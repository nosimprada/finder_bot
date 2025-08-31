import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers import routers
from middlewares.lang_middleware import LanguageMiddleware
from middlewares.message_log_middleware import MessageLogMiddleware
from utils.db import init_db
from utils.logging_bot import LoggingBot

async def main() -> None:
    bot = LoggingBot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.update.middleware(LanguageMiddleware(default_lang="en"))
    dp.message.middleware(MessageLogMiddleware())
    dp.include_routers(*routers)
    await dp.start_polling(bot)
    init_db()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())