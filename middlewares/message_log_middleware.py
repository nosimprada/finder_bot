from __future__ import annotations
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
import logging

from utils.message_log_store import log_user_message

logger = logging.getLogger("message_log_mw")

class MessageLogMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            try:
                chat_id = int(event.chat.id)
                msg_id = int(event.message_id)
                log_user_message(chat_id, msg_id)
                logger.debug("Logged USER message chat=%s msg_id=%s", chat_id, msg_id)
            except Exception:
                logger.exception("Failed to log incoming message")
        return await handler(event, data)
