import asyncio
import json
import logging
from pathlib import Path
import sys
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, OWNER_ID, refresh_owner_lang
from handlers import routers
from middlewares.lang_middleware import LanguageMiddleware
from middlewares.message_log_middleware import MessageLogMiddleware
from utils.db import init_db
from utils.logging_bot import LoggingBot

FILE_IDS_PATH = Path("data/file_ids.json")  
FILE_IDS_PATH.parent.mkdir(parents=True, exist_ok=True)

INSTRUCTION_PATH = Path("assets/instruction.mp4")
SOUND_MP3_PATH   = Path("assets/sound_password.mp3")

async def preload_telegram_file_ids(bot: Bot) -> None:
    from aiogram.types import FSInputFile
    import config as cfg  

    cache = {}
    if FILE_IDS_PATH.is_file():
        try:
            cache = json.loads(FILE_IDS_PATH.read_text(encoding="utf-8"))
        except Exception:
            cache = {}

    instr_id_prev = cache.get("instruction_video_file_id")
    sound_id_prev = cache.get("sound_mp3_file_id")

    instr_id = instr_id_prev
    sound_id = sound_id_prev

    if INSTRUCTION_PATH.is_file():
        try:
            msg = await bot.send_video(
                chat_id=OWNER_ID,
                video=FSInputFile(INSTRUCTION_PATH),
                caption="(preload) instruction.mp4"
            )
            if msg and msg.video and msg.video.file_id:
                instr_id = msg.video.file_id
            try:
                await bot.delete_message(chat_id=OWNER_ID, message_id=msg.message_id)
            except Exception:
                pass
        except Exception:
            pass

    if SOUND_MP3_PATH.is_file():
        try:
            msg = await bot.send_audio(
                chat_id=OWNER_ID,
                audio=FSInputFile(SOUND_MP3_PATH),
                caption="(preload) sound_password.mp3"
            )
            if msg and msg.audio and msg.audio.file_id:
                sound_id = msg.audio.file_id
            try:
                await bot.delete_message(chat_id=OWNER_ID, message_id=msg.message_id)
            except Exception:
                pass
        except Exception:
            pass

    if instr_id:
        cache["instruction_video_file_id"] = instr_id
    if sound_id:
        cache["sound_mp3_file_id"] = sound_id

    try:
        FILE_IDS_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    try:
        cfg.INSTRUCTION_VIDEO_FILE_ID = instr_id
        cfg.SOUND_MP3_FILE_ID = sound_id
    except Exception:
        pass
    
async def main() -> None:
    bot = LoggingBot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.update.middleware(LanguageMiddleware(default_lang="en"))
    dp.message.middleware(MessageLogMiddleware())
    dp.include_routers(*routers)

    await refresh_owner_lang(bot)
    await preload_telegram_file_ids(bot)
    await dp.start_polling(bot)
    init_db()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())