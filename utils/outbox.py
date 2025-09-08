from __future__ import annotations

import asyncio
from datetime import date
import json
from pathlib import Path
from typing import Optional

from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import INSTRUCTION_VIDEO_FILE_ID, OWNER_ID, OWNER_LANG, PET_NAME, PET_BIRTH_YEAR, PET_PHOTO_PATH, SOUND_MP3_FILE_ID, get_owner_lang
from keyboards.markup import kb_finder_share_location, kb_finder_welcome, kb_owner_contact, kb_owner_request_only, kb_owner_share_location, kb_sound_followup_finder, kb_sound_followup_owner, kb_sound_password
from utils import i18n
from utils.func import _calc_age_years
from utils.i18n import I18N as _I18N, I18n
from utils.translit import transliterate_pet_name

LIVE_LOCATION_VIDEO = Path(__file__).resolve().parents[1] / "assets" / "instruction.mp4"

FILE_IDS_PATH = Path("data/file_ids.json")

def _get_cached_file_id(key: str) -> str | None:
    try:
        if not FILE_IDS_PATH.is_file():
            return None
        data = json.loads(FILE_IDS_PATH.read_text(encoding="utf-8"))
        val = data.get(key)
        return val if isinstance(val, str) and val else None
    except Exception:
        return None

#UNIVERSAL

async def send_live_location_instructions(
    *,
    message: Optional[Message] = None,
    bot: Optional[Bot] = None,
    chat_id: Optional[int] = None,
    lang: str,
    i18n: Optional[I18n] = None,
) -> None:
    i18n = i18n or _I18N
    text = i18n.t(lang, "live_location_howto")

    async def _send_video(_bot: Bot, _chat_id: int) -> None:
        cached_id = _get_cached_file_id("instruction_video_file_id")
        if cached_id:
            print('айди есть в кеше')
            await _bot.send_video(chat_id=_chat_id, video=cached_id, caption=text)
            return
        if LIVE_LOCATION_VIDEO.is_file():
            print('айди нет в кеше')
            await _bot.send_video(chat_id=_chat_id, video=FSInputFile(LIVE_LOCATION_VIDEO), caption=text)
            return
        # 3) fallback — просто текст
        await _bot.send_message(chat_id=_chat_id, text=text)

    if message is not None:
        await _send_video(message.bot, message.chat.id)
        return

    if bot is None or chat_id is None:
        raise ValueError("Provide either `message` or (`bot` and `chat_id`).")

    await _send_video(bot, chat_id)

async def send_proximity_notification(
    bot: Bot,
    chat_id: int,
    lang: str,
    i18n: I18n | None = None,
) -> None:
    i18n = i18n or _I18N
    await bot.send_message(
        chat_id=chat_id,
        text=i18n.t(lang, "proximity_notification"),  # ключ в локалях
        reply_markup=kb_sound_password(lang, i18n),
    )


SOUND_PASSWORD_FILE = Path(__file__).resolve().parents[1] / "assets" / "sound_password.mp3"


async def send_sound_password_for_owner(bot: Bot, chat_id: int, lang: str, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    try:
        await bot.send_message(chat_id, "*==============================*")
    except Exception:
        pass

    try:
        cached_id = _get_cached_file_id("sound_mp3_file_id")
        if cached_id:
            await bot.send_audio(chat_id, audio=cached_id)
        elif SOUND_PASSWORD_FILE.is_file():
            await bot.send_audio(chat_id, audio=FSInputFile(SOUND_PASSWORD_FILE))
        else:
            await bot.send_message(chat_id, "Файл звукового пароля не найден.")
    except Exception:
        pass

    await asyncio.sleep(30)
    try:
        await bot.send_message(
            chat_id,
            i18n.t(lang, "after_sound_prompt"),
            reply_markup=kb_sound_followup_owner(lang, i18n),
        )
    except Exception:
        pass


async def send_sound_password_for_finder(bot: Bot, chat_id: int, lang: str, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    try:
        await bot.send_message(chat_id, "*==============================*")
    except Exception:
        pass

    try:
        cached_id = _get_cached_file_id("sound_mp3_file_id")
        if cached_id:
            await bot.send_audio(chat_id, audio=cached_id)
        elif SOUND_PASSWORD_FILE.is_file():
            await bot.send_audio(chat_id, audio=FSInputFile(SOUND_PASSWORD_FILE))
        else:
            await bot.send_message(chat_id, "Файл звукового пароля не найден.")
    except Exception:
        pass

    await asyncio.sleep(30)
    try:
        await bot.send_message(
            chat_id,
            i18n.t(lang, "after_sound_prompt"),
            reply_markup=kb_sound_followup_finder(lang, i18n),
        )
    except Exception:
        pass


    
#FINDER

async def send_finder_pet_card(message: Message, lang: str, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    age = _calc_age_years(PET_BIRTH_YEAR)

    # Транслитерация имени питомца
    pet_name_display = transliterate_pet_name(PET_NAME, lang)

    caption = i18n.t(lang, "pet_info_message", pet_name=pet_name_display, age=age)

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

async def send_finder_owner_alerted(message: Message, lang: str, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    await message.answer(i18n.t(lang, "owner_alerted"))

async def notify_owner_finder_live_received(bot: Bot, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    await bot.send_message(
        chat_id=int(OWNER_ID),
        text=i18n.t(get_owner_lang(), "finder_live_received"),
        reply_markup=kb_owner_share_location(get_owner_lang(), i18n),  # <- вот тут кнопка
    )

async def notify_owner_about_finder(bot: Bot, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    text = i18n.t(get_owner_lang(), "owner_found_pet") + "\n\n👇"

    await bot.send_message(
            chat_id=OWNER_ID,
            text="*==============================*",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text="Завершить чат")]],
                resize_keyboard=True
            )
        )
    photo_path = Path(PET_PHOTO_PATH)
    if photo_path.is_file():
        await bot.send_photo(
            chat_id=OWNER_ID,
            photo=FSInputFile(photo_path),
            caption=text,
            reply_markup=kb_owner_contact(get_owner_lang(), i18n),
        )
    else:
        await bot.send_message(
            chat_id=OWNER_ID,
            text=text,
            reply_markup=kb_owner_contact(get_owner_lang(), i18n),
        )

async def notify_finder_request_location(
    bot: Bot,
    finder_id: int,
    finder_lang: str,
    i18n: I18n | None = None,
) -> None:
    i18n = i18n or _I18N
    await bot.send_message(
        chat_id=int(finder_id),
        text=i18n.t(finder_lang, "location_requested"),
        reply_markup=kb_finder_share_location(finder_lang, i18n),
    )


#------------OWNER------------

async def send_owner_request_menu(message: Message, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    await message.answer(
        i18n.t(get_owner_lang(), "location_instruction"),
        reply_markup=kb_owner_request_only(get_owner_lang(), i18n),
    )

async def send_owner_location_requested(message: Message, i18n: I18n | None = None) -> None:
    i18n = i18n or _I18N
    await message.answer(i18n.t(get_owner_lang(), "location_requested_from_owner"))