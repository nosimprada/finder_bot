from __future__ import annotations

from datetime import date
from pathlib import Path

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config import (
    OWNER_ID,
    OWNER_LANG,
    START_KEY,
    Stage,
    get_owner_lang,
)

from utils.finder_store import (
    enqueue,
    ensure_finder,
    get_finder,
    set_lang as store_set_lang,
    set_stage, get_stage,
    status_of,
)
from utils.func import _extract_start_arg, _pick_lang
from utils.i18n import I18N as _I18N, I18n
from utils.location_watcher import ensure_watcher_for_pair, set_finder_live
from utils.message_log_store import clear_chat, delete_all_logged_messages, delete_logged_bot_messages
from utils.outbox import notify_finder_request_location, notify_owner_about_finder, notify_owner_finder_live_received, send_finder_owner_alerted, send_finder_pet_card, send_live_location_instructions

router = Router(name="finder")



@router.message(CommandStart())
async def start_any(message: Message, state: FSMContext, lang: str):
    
    print(message.from_user.language_code)
    uid = message.from_user.id
    if int(uid) == int(OWNER_ID):
        return

    arg = _extract_start_arg(message.text)
    i18n = _I18N

    if arg == str(START_KEY):
        ensure_finder(uid, lang=str(lang), stage=int(Stage.START_SCREEN))
        store_set_lang(uid, lang)
        await send_finder_pet_card(message, lang, i18n)
        set_stage(uid, Stage.FINDER_WELCOME_SHOWN)
        return

    row = get_finder(uid)
    if not row:
        return

    store_set_lang(uid, lang)

    cur_stage = get_stage(uid)

    if cur_stage == int(Stage.FINDER_PRESSED_CONTACT_OWNER):
        await send_finder_owner_alerted(message, lang, i18n)
        return

    if cur_stage == int(Stage.OWNER_REQUESTED_FINDER_LOCATION):
        await notify_finder_request_location(
            bot=message.bot,
            finder_id=uid,
            finder_lang=lang,
            i18n=i18n
        )
        return

    if cur_stage == int(Stage.THE_FINDER_WAS_SHOWN_INSTRUCTIONS_FOR_SENDING_THE_LOCATION):
        await send_live_location_instructions(message=message, lang=lang)
        try:
            await state.set_state(FinderStates.WAITING_LIVE)
        except Exception:
            pass
        return

    await send_finder_pet_card(message, lang, i18n)
    if cur_stage in (None, int(Stage.NONE), int(Stage.START_SCREEN)):
        set_stage(uid, Stage.FINDER_WELCOME_SHOWN)


@router.callback_query(F.data == "finder:contact_owner")
async def finder_contact_owner(cb: CallbackQuery):
    uid = cb.from_user.id
    lang = _pick_lang(getattr(cb.from_user, "language_code", None))
    i18n = _I18N

    if int(uid) == int(OWNER_ID):
        return

    st, _pos = status_of(uid)  # 'blocked'|'active'|'queued'|'completed'|'none'
    if st in ("blocked", "active", "queued"):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        qpos = enqueue(uid, lang=lang)
    except RuntimeError:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    set_stage(uid, Stage.FINDER_PRESSED_CONTACT_OWNER)

    if qpos == 1:
        try:
            await notify_owner_about_finder(cb.bot, i18n)
        except Exception:
            pass

    try:
        await cb.answer()
    except Exception:
        pass

    try:
        await cb.message.answer(i18n.t(lang, "owner_alerted"))
    except Exception:
        pass


# --- FSM состояния нашедшего ---
class FinderStates(StatesGroup):
    WAITING_LIVE = State()   


@router.callback_query(F.data == "finder:share_location")
async def finder_share_location(cb: CallbackQuery, state: FSMContext):
    uid = cb.from_user.id
    if int(uid) == int(OWNER_ID):
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await cb.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    lang = (getattr(cb.from_user, "language_code", None) or "en").split("-")[0].lower()
    # if lang not in ("ru", "en"):
    #     lang = "en"

    await send_live_location_instructions(message=cb.message, lang=lang)

    try:
        await state.set_state(FinderStates.WAITING_LIVE)
    except Exception:
        pass

    try:
        set_stage(uid, Stage.THE_FINDER_WAS_SHOWN_INSTRUCTIONS_FOR_SENDING_THE_LOCATION)
    except Exception:
        pass

    try:
        await cb.answer()
    except Exception:
        pass


# === ПРИЁМ локации нашедшего ===

@router.message(FinderStates.WAITING_LIVE, F.location)
async def finder_live_location_received(message: Message, state: FSMContext):
    #  фильтр
    if int(message.from_user.id) == int(OWNER_ID):
        return

    lang = _pick_lang(getattr(message.from_user, "language_code", None))
    i18n = _I18N
    live_period = getattr(message.location, "live_period", None)

    if not live_period:
        try:
            await send_live_location_instructions(message=message, lang=lang)
        except Exception:
            pass
        return

    # 1) сохр live в FSM
    try:
        await state.update_data(
            finder_live={
                "chat_id": message.chat.id,
                "message_id": message.message_id,
                "latitude": message.location.latitude,
                "longitude": message.location.longitude,
                "live_period": int(live_period),
            }
        )
    except Exception:
        pass

    # 2) обновляем точку нашедшего для watcher
    try:
        set_finder_live(
            finder_id=message.from_user.id,
            lat=message.location.latitude,
            lon=message.location.longitude,
            live_period_sec=int(live_period),
        )
    except Exception:
        pass

    # 3) запуск watcher для пары 
    try:
        ensure_watcher_for_pair(
            bot=message.bot,
            owner_id=int(OWNER_ID),
            finder_id=int(message.from_user.id),
            owner_lang=get_owner_lang(),
            finder_lang=lang,
            i18n=i18n,
        )
    except Exception:
        pass

    # 4) увед один раз
    try:
        data = await state.get_data()
        if not data.get("owner_notified_finder_live"):
            await notify_owner_finder_live_received(message.bot, i18n)
            await state.update_data(owner_notified_finder_live=True)
    except Exception:
        pass

    # 5) подтверждение нашедшему
    try:
        await message.answer(i18n.t(lang, "location_shared_response"))
    except Exception:
        pass


@router.edited_message(FinderStates.WAITING_LIVE, F.location)
async def finder_live_location_edited(message: Message, state: FSMContext):
    if int(message.from_user.id) == int(OWNER_ID):
        return

    try:
        await state.update_data(
            finder_live={
                "chat_id": message.chat.id,
                "message_id": message.message_id,
                "latitude": message.location.latitude,
                "longitude": message.location.longitude,
                "live_period": int(getattr(message.location, "live_period", 0) or 0),
            }
        )
    except Exception:
        pass

    try:
        set_finder_live(
            finder_id=message.from_user.id,
            lat=message.location.latitude,
            lon=message.location.longitude,
            live_period_sec=int(getattr(message.location, "live_period", 0) or 0),
        )
    except Exception:
        pass


@router.message(FinderStates.WAITING_LIVE)
async def finder_waiting_live_any_other(message: Message, state: FSMContext):
    if int(message.from_user.id) == int(OWNER_ID):
        return

    lang = _pick_lang(getattr(message.from_user, "language_code", None))
    try:
        await send_live_location_instructions(message=message, lang=lang)
    except Exception:
        pass