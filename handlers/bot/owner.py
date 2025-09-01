# handlers/bot/owner.py
from __future__ import annotations
from pathlib import Path

from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from config import OWNER_ID, OWNER_LANG, Stage
from keyboards.markup import kb_finder_share_location, kb_owner_action_menu
from utils.i18n import I18N as _I18N
from utils.finder_store import get_active, get_finder, get_stage, set_stage

router = Router(name="owner")


@router.callback_query(F.data == "owner:contact")
async def owner_contact(cb: CallbackQuery):
    """
    Нажатие владельцем кнопки «Связаться»:
    - принимать только от OWNER_ID;
    - если есть активный нашедший и стадия ещё не OWNER_ACTION_MENU —
      показываем меню действий и переводим нашедшего на stage OWNER_ACTION_MENU;
    - в любом случае удаляем клавиатуру у исходного сообщения с кнопкой «Связаться»,
      чтобы повторно нажать было нельзя;
    - повторные нажатия просто игнорим.
    """
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
        await cb.message.answer(
            i18n.t(OWNER_LANG, "location_instruction"),
            reply_markup=kb_owner_action_menu(OWNER_LANG, i18n),
        )
    except Exception:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        set_stage(active_finder_id, Stage.OWNER_ACTION_MENU)
    except Exception:
        pass

    try:
        await cb.answer()
    except Exception:
        pass



@router.callback_query(F.data == "owner:ask_location")
async def owner_ask_location(cb: CallbackQuery):
    """
    Владелец нажал «Узнать локацию питомца»:
      - только от OWNER_ID;
      - убираем клавиатуру у сообщения;
      - нашедшему шлём просьбу поделиться локацией + кнопку;
      - ставим нашедшему stage = OWNER_REQUESTED_FINDER_LOCATION;
      - владельцу пишем «Локация запрошена, ожидайте ответа».
    """
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

    finder_row = get_finder(finder_id) or {}
    finder_lang = (finder_row.get("lang") or "en")

    try:
        await cb.bot.send_message(
            chat_id=int(finder_id),
            text=i18n.t(finder_lang, "location_instruction"),
            reply_markup=kb_finder_share_location(finder_lang, i18n),
        )
    except Exception:
        pass

    try:
        set_stage(finder_id, Stage.OWNER_REQUESTED_FINDER_LOCATION)
    except Exception:
        pass

    try:
        await cb.message.answer(i18n.t(OWNER_LANG, "location_requested"))
    except Exception:
        pass
    try:
        await cb.answer()
    except Exception:
        pass

LIVE_LOCATION_VIDEO = Path(__file__).resolve().parents[2] / "assets" / "instruction.mp4"

@router.callback_query(F.data == "owner:send_location")
async def owner_send_location(cb: CallbackQuery):
    """
    Владелец нажал «Отправить мою локацию»:
      - только OWNER_ID;
      - убираем inline-клавиатуру у сообщения;
      - отправляем овнеру инструкцию + видео из assets/live_location.mp4 (если есть).
    """
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
    text = i18n.t(OWNER_LANG, "live_location_howto")

    try:
        if LIVE_LOCATION_VIDEO.is_file():
            await cb.message.answer_video(
                video=FSInputFile(LIVE_LOCATION_VIDEO),
                caption=text,
            )
        else:
            await cb.message.answer(text)
    except Exception:
        try:
            await cb.answer()
        except Exception:
            pass
        return

    try:
        await cb.answer()
    except Exception:
        pass