from __future__ import annotations
import asyncio
from pathlib import Path

from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ChatMemberUpdated 

from config import GROUP_CHAT_ID, GROUP_INVITE_LINK, OWNER_ID, OWNER_LANG, Stage, get_owner_lang
from keyboards.markup import kb_finder_share_location, kb_open_group_link, kb_owner_arrival_menu, kb_owner_chat_consent, kb_sound_followup_finder, kb_sound_followup_owner
from utils.func import _pick_lang, _select_time_text
from utils.i18n import I18N as _I18N
from utils.finder_store import finish_active, get_active, get_finder, get_stage, set_stage
from utils.location_watcher import ensure_watcher_for_pair, get_finder_point, get_owner_point, set_owner_live
from utils.message_log_store import clear_chat, delete_all_logged_messages
from utils.outbox import notify_finder_request_location, send_finder_pet_card, send_live_location_instructions, send_owner_location_requested, send_owner_request_menu, send_sound_password_for_finder, send_sound_password_for_owner

router = Router(name="owner")


@router.callback_query(F.data == "owner:contact")
async def owner_contact(cb: CallbackQuery):
    # только владелец
    if int(cb.from_user.id) != int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    active_finder_id = get_active()
    if not active_finder_id:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    cur_stage = get_stage(active_finder_id)
    if cur_stage == int(Stage.OWNER_ACTION_MENU):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    i18n = _I18N

    try:
        await send_owner_request_menu(cb.message, i18n)
    except Exception:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        set_stage(active_finder_id, Stage.FINDER_PRESSED_CONTACT_OWNER)
    except Exception:
        pass

    try:
        await cb.answer()
    except Exception:
        pass



@router.callback_query(F.data == "owner:ask_location")
async def owner_ask_location(cb: CallbackQuery):
    if int(cb.from_user.id) != int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    finder_id = get_active()
    if not finder_id:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    i18n = _I18N

    # язык нашедшего
    finder_row = get_finder(finder_id) or {}
    finder_lang = (finder_row.get("lang") or "en")

    try:
        await notify_finder_request_location(cb.bot, finder_id, finder_lang, i18n)
    except Exception:
        pass

    # этап нашедшего
    try:
        set_stage(finder_id, Stage.OWNER_REQUESTED_FINDER_LOCATION)
    except Exception:
        pass

    try:
        await send_owner_location_requested(cb.message, i18n)
    except Exception:
        pass

    try:
        await cb.answer()
    except Exception:
        pass

# --- FSM состояния владельца ---
class OwnerStates(StatesGroup):
    WAITING_LIVE = State()   

LIVE_LOCATION_VIDEO = Path(__file__).resolve().parents[2] / "assets" / "instruction.mp4"

@router.callback_query(F.data == "owner:share_location")
async def owner_send_location(cb: CallbackQuery, state: FSMContext):
    if int(cb.from_user.id) != int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    i18n = _I18N
    text = i18n.t(get_owner_lang(), "live_location_howto")

    try:
        await send_live_location_instructions(message=cb.message, lang=get_owner_lang())
        # if LIVE_LOCATION_VIDEO.is_file():
        #     await cb.message.answer_video(
        #         video=FSInputFile(LIVE_LOCATION_VIDEO),
        #         caption=text,
        #     )
        # else:
        #     await cb.message.answer(text)
    except Exception:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await state.set_state(OwnerStates.WAITING_LIVE)
    except Exception:
        pass

    # finder_id = get_active()
    # if finder_id:
    #     try:
    #         finder_row = get_finder(finder_id) or {}
    #         finder_lang = (finder_row.get("lang") or "en")

    #         await cb.bot.send_message(
    #             chat_id=int(finder_id),
    #             text=i18n.t(finder_lang, "request_location"),
    #             reply_markup=kb_finder_share_location(finder_lang, i18n),
    #         )
    #         set_stage(finder_id, Stage.OWNER_REQUESTED_FINDER_LOCATION)
    #     except Exception:
    #         pass

    try:
        await cb.answer()
    except Exception:
        pass

# === ПРИЁМ локации владельца ===

@router.message(OwnerStates.WAITING_LIVE, F.location)
async def owner_live_location_received(message: Message, state: FSMContext):
    i18n = _I18N
    live_period = getattr(message.location, "live_period", None)
    print(f"[OWNER LIVE] message from={message.from_user.id} live_period={live_period} "
          f"coords=({message.location.latitude},{message.location.longitude})")

    if not live_period:
        await message.answer(i18n.t(get_owner_lang(), "live_location_howto"))
        return

    try:
        await state.update_data(
            owner_live={
                "chat_id": message.chat.id,
                "message_id": message.message_id,
                "latitude": message.location.latitude,
                "longitude": message.location.longitude,
                "live_period": int(live_period),
            }
        )
    except Exception:
        pass

    try:
        set_owner_live(
            owner_id=int(message.from_user.id),
            lat=message.location.latitude,
            lon=message.location.longitude,
            live_period_sec=min(int(live_period), 86400),
        )
        print("[OWNER LIVE] set_owner_live() called")
    except Exception as e:
        print(f"[OWNER LIVE] set_owner_live error: {e}")

    try:
        finder_id = get_active()
        if finder_id:
            finder_row = get_finder(finder_id) or {}
            finder_lang = (finder_row.get("lang") or "en")
            ensure_watcher_for_pair(
                bot=message.bot,
                owner_id=int(message.from_user.id),
                finder_id=int(finder_id),
                owner_lang=get_owner_lang(),
                finder_lang=finder_lang,
                i18n=i18n,
                #test_force_close_after_sec=60,
            )
            print(f"[OWNER LIVE] ensure_watcher_for_pair(owner={message.from_user.id}, finder={finder_id})")

            try:
                fp = get_finder_point(int(finder_id))
                if fp:
                    await message.bot.send_location(
                        chat_id=message.chat.id,
                        latitude=fp.lat,
                        longitude=fp.lon,
                    )
            except Exception as e:
                print(f"[OWNER LIVE] send last finder location error: {e}")

            try:
                await message.answer(i18n.t(get_owner_lang(), "navigation_hint_owner"))
            except Exception:
                pass

            try:
                await asyncio.sleep(5)
                # «Сообщите, когда вы прибудете. ...»
                await message.answer(
                    i18n.t(get_owner_lang(), "navigation_hint_user"),
                    reply_markup=kb_owner_arrival_menu(get_owner_lang(), i18n),
                )
            except Exception:
                pass

    except Exception as e:
        print(f"[OWNER LIVE] ensure_watcher_for_pair error: {e}")

    # 4) подтверждение владельцу
    # try:
    #     await message.answer(i18n.t(OWNER_LANG, "owner_location_sent"))
    # except Exception:
    #     pass


@router.edited_message(OwnerStates.WAITING_LIVE, F.location)
async def owner_live_location_edited(message: Message, state: FSMContext):
    # пускаем только владельца
    if int(message.from_user.id) != int(OWNER_ID):
        return

    live_period = getattr(message.location, "live_period", 0) or 0
    print(f"[OWNER LIVE EDIT] message from={message.from_user.id} live_period={live_period} "
          f"coords=({message.location.latitude},{message.location.longitude})")

    try:
        await state.update_data(
            owner_live={
                "chat_id": message.chat.id,
                "message_id": message.message_id,
                "latitude": message.location.latitude,
                "longitude": message.location.longitude,
                "live_period": int(live_period),
            }
        )
    except Exception:
        pass

    try:
        set_owner_live(
            owner_id=int(message.from_user.id),
            lat=message.location.latitude,
            lon=message.location.longitude,
            live_period_sec=min(int(live_period), 86400),
        )
        print("[OWNER LIVE EDIT] set_owner_live() called")
    except Exception as e:
        print(f"[OWNER LIVE EDIT] set_owner_live error: {e}")



@router.callback_query(F.data.startswith("owner:eta:"))
async def owner_eta_choice(cb: CallbackQuery):
    # только владелец
    if int(cb.from_user.id) != int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    # извлекаем выбранное значение (10/20/30/1h)
    try:
        tail = cb.data.split(":")[-1]
        if tail == "1h":
            minutes = 60
            is_hour = True
        else:
            minutes = int(tail)
            is_hour = False
    except Exception:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    if minutes not in (10, 20, 30, 60):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    # убрать старую клавиатуру
    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    i18n = _I18N

    # кому писать — активный finder
    finder_id = get_active()
    if finder_id:
        finder_row = get_finder(finder_id) or {}
        finder_lang = (finder_row.get("lang") or "en")

        eta_key_map = {
            10: "arrival_owner_10",
            20: "arrival_owner_20",
            30: "arrival_owner_30",
            60: "arrival_owner_60",   
        }
        eta_key = eta_key_map.get(minutes)

        try:
            await cb.bot.send_message(
                chat_id=int(finder_id),
                text=i18n.t(finder_lang, eta_key),
            )
        except Exception:
            pass

        try:
            await cb.message.answer(
                i18n.t(
                    get_owner_lang(),
                    "arrival_timer_warning",
                    select_time=_select_time_text(get_owner_lang(), minutes),
                ),
                reply_markup=kb_owner_arrival_menu(get_owner_lang(), i18n),
            )
        except Exception:
            pass

    try:
        await cb.answer()
    except Exception:
        pass


#CHAT
@router.callback_query(F.data == "owner:start_chat")
async def owner_start_chat(cb: CallbackQuery):
    if int(cb.from_user.id) != int(OWNER_ID):
        try: await cb.answer()
        except: pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    i18n = _I18N
    try:
        await cb.message.answer(
            i18n.t(get_owner_lang(), "language_warning"),
            reply_markup=kb_owner_chat_consent(get_owner_lang(), i18n),
        )
    except Exception:
        pass

    try: await cb.answer()
    except: pass


@router.callback_query(F.data == "owner:chat_back")
async def owner_chat_back(cb: CallbackQuery):
    if int(cb.from_user.id) != int(OWNER_ID):
        try: await cb.answer()
        except: pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    i18n = _I18N
    try:
        await cb.message.answer(
            i18n.t(get_owner_lang(), "arrival_timer_warning"),
            reply_markup=kb_owner_arrival_menu(OWNER_LANG, i18n),
        )
    except Exception:
        pass

    try: await cb.answer()
    except: pass


@router.callback_query(F.data == "owner:chat_accept")
async def owner_chat_accept(cb: CallbackQuery):
    if int(cb.from_user.id) != int(OWNER_ID):
        try: await cb.answer()
        except: pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    i18n = _I18N

    finder_id = get_active()
    if finder_id:
        finder_row = get_finder(finder_id) or {}
        finder_lang = (finder_row.get("lang") or "en")

        try:
            await cb.bot.send_message(
                chat_id=int(finder_id),
                text=i18n.t(finder_lang, "owner_chat_offer"),
                reply_markup=kb_open_group_link(finder_lang, GROUP_INVITE_LINK, i18n),
            )
        except Exception:
            pass

    # опционально можно подтвердить владельцу:
    # try:
    #     await cb.message.answer(i18n.t(OWNER_LANG, "invite_sent_owner"))
    # except Exception:
    #     pass

    try: await cb.answer()
    except: pass


@router.chat_member()
async def on_finder_joined_group(event: ChatMemberUpdated):
    if int(event.chat.id) != int(GROUP_CHAT_ID):
        return

    old_status = getattr(event.old_chat_member, "status", None)
    new_status = getattr(event.new_chat_member, "status", None)

    if old_status not in ("left", "kicked") or new_status not in ("member", "administrator"):
        return

    # сверяем, что вошёл именно активный нашедший
    active_finder_id = get_active()
    joined_user_id = event.new_chat_member.user.id
    if not active_finder_id or int(joined_user_id) != int(active_finder_id):
        return

    i18n = _I18N
    # уведомляем владельца + кнопка с ссылкой на чат
    try:
        await event.bot.send_message(
            chat_id=int(OWNER_ID),
            text=i18n.t(get_owner_lang(), "chat_partner_joined_owner"),
            reply_markup=kb_open_group_link(get_owner_lang(), GROUP_INVITE_LINK, i18n),
        )
    except Exception:
        pass



#Звук 

@router.callback_query(F.data == "sound:password")
async def sound_password_pressed(cb: CallbackQuery):
    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    i18n = _I18N
    lang = _pick_lang(getattr(cb.from_user, "language_code", None))

    if int(cb.from_user.id) == int(OWNER_ID):
        await send_sound_password_for_owner(cb.bot, cb.message.chat.id, get_owner_lang(), i18n)
    else:
        await send_sound_password_for_finder(cb.bot, cb.message.chat.id, lang, i18n)

    try:
        await cb.answer()
    except Exception:
        pass


@router.callback_query(F.data == "sound:done")
async def sound_mission_done(cb: CallbackQuery):
    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    chat_id = cb.message.chat.id
    user_id = cb.from_user.id

    # 2) удалить всю зафиксированную историю сообщений в чате
    try:
        await delete_all_logged_messages(cb.bot, chat_id)
    except Exception:
        pass

    if int(user_id) == int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    i18n = _I18N
    lang = None
    try:
        row = get_finder(user_id) or {}
        lang = row.get("lang") or (cb.from_user.language_code or "en")
    except Exception:
        lang = (cb.from_user.language_code or "en")

    try:
        await send_finder_pet_card(cb.message, lang, i18n)
    except Exception:
        pass

    try:
        active_id = get_active()
        if active_id and str(active_id) == str(user_id):
            finish_active(mark_completed=True)
    except Exception:
        pass

    try:
        await cb.answer()
    except Exception:
        pass


@router.callback_query(F.data == "sound:check_owner")
async def sound_check_owner_location(cb: CallbackQuery):
    i18n = _I18N
    lang = _pick_lang(getattr(cb.from_user, "language_code", None))

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    sent_ok = False
    try:
        pt = get_owner_point(int(OWNER_ID))
        if pt:
            await cb.bot.send_location(
                chat_id=cb.message.chat.id,
                latitude=pt.lat,
                longitude=pt.lon,
            )
            sent_ok = True
        else:
            await cb.message.answer(i18n.t(lang, "owner_location_unavailable"))
    except Exception:
        pass

    if sent_ok:
        try:
            await cb.bot.send_message(
                cb.message.chat.id,
                i18n.t(lang, "after_sound_prompt"),
                reply_markup=kb_sound_followup_finder(lang, i18n),  # для нашедшего
            )
        except Exception:
            pass

    try:
        await cb.answer()
    except Exception:
        pass


@router.callback_query(F.data == "sound:check_finder")
async def sound_check_finder_location(cb: CallbackQuery):
    i18n = _I18N

    # только владелец
    if int(cb.from_user.id) != int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    sent_ok = False
    try:
        finder_id = get_active()
        if finder_id:
            pt = get_finder_point(int(finder_id))
            if pt:
                await cb.bot.send_location(
                    chat_id=cb.message.chat.id,
                    latitude=pt.lat,
                    longitude=pt.lon,
                )
                sent_ok = True
            else:
                await cb.message.answer(i18n.t(get_owner_lang(), "finder_location_unavailable"))
        else:
            await cb.message.answer(i18n.t(get_owner_lang(), "finder_location_unavailable"))
    except Exception:
        pass

    if sent_ok:
        try:
            await cb.bot.send_message(
                cb.message.chat.id,
                i18n.t(get_owner_lang(), "after_sound_prompt"),
                reply_markup=kb_owner_arrival_menu(get_owner_lang(), i18n),  # для владельца
            )
        except Exception:
            pass

    try:
        await cb.answer()
    except Exception:
        pass