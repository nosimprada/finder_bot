from __future__ import annotations

from datetime import date
from pathlib import Path

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

from config import (
    OWNER_ID,
    OWNER_LANG,
    START_KEY,
    PET_NAME,
    PET_BIRTH_YEAR,
    PET_PHOTO_PATH,
    Stage,
)

from utils.finder_store import (
    enqueue,
    ensure_finder,
    get_finder,
    set_lang as store_set_lang,
    set_stage, get_stage,
    status_of,
)
from utils.i18n import I18N as _I18N, I18n
from keyboards.markup import (
    kb_finder_welcome,
    kb_owner_contact,   # <-- добавили импорт
)
from utils.message_log_store import clear_chat, delete_all_logged_messages, delete_logged_bot_messages

router = Router(name="finder")


def _extract_start_arg(text: str | None) -> str:
    if not text:
        return ""
    parts = text.strip().split(maxsplit=1)
    return parts[1].strip() if len(parts) == 2 else ""

def _pick_lang(code: str | None) -> str:
    if not code:
        return "en"
    code = code.lower()
    if code.startswith("ru"):
        return "ru"
    return "en"

def _calc_age_years(birth_year: int) -> int:
    return max(0, int(date.today().year) - int(birth_year))

async def _send_finder_welcome(message: Message, lang: str, i18n: I18n) -> None:
    age = _calc_age_years(PET_BIRTH_YEAR)
    caption = i18n.t(lang, "pet_info_message", pet_name=PET_NAME, age=age)

    photo_path = Path(PET_PHOTO_PATH)
    if photo_path.is_file():
        await message.answer_photo(
            photo=FSInputFile(photo_path),
            caption=caption,
            reply_markup=kb_finder_welcome(lang, i18n),
        )
    else:
        await message.answer(
            caption,
            reply_markup=kb_finder_welcome(lang, i18n),
        )


async def _notify_owner_about_finder(bot, i18n: I18n) -> None:
    """
    Сообщение владельцу по ТЗ: без упоминания нашедшего.
    Текст из локалей + указатель на кнопку ниже.
    """
    text = i18n.t(OWNER_LANG, "owner_found_pet") + "\n\n👇"

    photo_path = Path(PET_PHOTO_PATH)
    if photo_path.is_file():
        await bot.send_photo(
            chat_id=OWNER_ID,
            photo=FSInputFile(photo_path),
            caption=text,
            reply_markup=kb_owner_contact(OWNER_LANG, i18n),   # <-- используем клавиатуру из markup
        )
    else:
        await bot.send_message(
            chat_id=OWNER_ID,
            text=text,
            reply_markup=kb_owner_contact(OWNER_LANG, i18n),   # <-- используем клавиатуру из markup
        )



@router.message(CommandStart())
async def start_any(message: Message):
    uid = message.from_user.id
    if int(uid) == int(OWNER_ID):
        return

    arg = _extract_start_arg(message.text)
    lang = _pick_lang(getattr(message.from_user, "language_code", None))
    i18n = _I18N

    if arg == str(START_KEY):
        ensure_finder(uid, lang=str(lang), stage=int(Stage.START_SCREEN))
        store_set_lang(uid, lang)

        await _send_finder_welcome(message, lang, i18n)
        set_stage(uid, Stage.FINDER_WELCOME_SHOWN)
        return

    row = get_finder(uid)
    if not row:
        return

    store_set_lang(uid, lang)

    cur_stage = get_stage(uid)
    if cur_stage == int(Stage.FINDER_PRESSED_CONTACT_OWNER):
        await message.answer(i18n.t(lang, "owner_alerted"))
        return

    await _send_finder_welcome(message, lang, i18n)
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
            await _notify_owner_about_finder(cb.bot, i18n)
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
