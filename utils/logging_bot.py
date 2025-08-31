from __future__ import annotations

import logging
from typing import TypeVar, Optional
from aiogram import Bot
from aiogram.methods import TelegramMethod
from aiogram.types import Message, MessageId
from utils.message_log_store import log_bot_message

T = TypeVar("T")
log = logging.getLogger("logging_bot")

class LoggingBot(Bot):
    async def __call__(
        self,
        method: TelegramMethod[T],
        request_timeout: Optional[int] = None,
        **kwargs,
    ) -> T:
        result: T = await super().__call__(method, request_timeout=request_timeout, **kwargs)

        try:
            if isinstance(result, Message):
                chat_id = str(result.chat.id)
                log_bot_message(chat_id, result.message_id)

            elif isinstance(result, list) and result and isinstance(result[0], Message):
                for m in result:
                    log_bot_message(str(m.chat.id), m.message_id)

            elif isinstance(result, MessageId):
                chat_id = getattr(method, "chat_id", None) \
                          or getattr(method, "chat", None) \
                          or getattr(method, "target_chat_id", None)
                if chat_id is not None:
                    log_bot_message(str(chat_id), result.message_id)
        except Exception:
            pass

        return result
