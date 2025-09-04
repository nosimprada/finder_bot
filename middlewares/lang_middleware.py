from __future__ import annotations
from typing import Callable, Dict, Any, Awaitable, Optional
from aiogram import BaseMiddleware, Bot
from aiogram.types import Chat
import logging

from utils.i18n import I18N     
from utils.finder_store import set_lang
from config import OWNER_ID

logger = logging.getLogger("lang_middleware")


def _normalize_lang_code(raw: Optional[str], default: str = "en") -> str:
    if not raw:
        return default
    code = raw.strip().replace("_", "-").lower()

    alias_map = {
        "iw": "he",   # иврит
        "in": "id",   # индонезийский
        "ua": "uk",   
    }
    if code in alias_map:
        return alias_map[code]

    base = code.split("-", 1)[0]

    if code.startswith("zh-"):
        return "zh"

    return base or default


class LanguageMiddleware(BaseMiddleware):
    def __init__(self, default_lang: str = "en", prefer_chat_member: bool = True):
        super().__init__()
        self.default_lang = default_lang
        self.prefer_chat_member = prefer_chat_member
        logger.info("[LanguageMW:init] default=%r prefer_chat_member=%s",
                    self.default_lang, self.prefer_chat_member)

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        if "t" in data and "lang" in data:
            return await handler(event, data)

        user = data.get("event_from_user")
        chat: Chat | None = data.get("event_chat")
        bot: Bot | None = data.get("bot")

        raw = getattr(user, "language_code", None) if user else None

        if self.prefer_chat_member and bot and chat and user:
            try:
                cm = await bot.get_chat_member(chat_id=chat.id, user_id=user.id)
                raw_cm = getattr(cm.user, "language_code", None)
                if raw_cm:
                    raw = raw_cm
                logger.info("[LanguageMW] get_chat_member lang=%r, update lang=%r",
                            raw_cm, getattr(user, "language_code", None))
            except Exception as e:
                logger.info("[LanguageMW] get_chat_member failed: %s", e)

        chosen = _normalize_lang_code(raw, self.default_lang)

        data["lang"] = chosen
        data["t"] = lambda key, **kw: I18N.t(chosen, key, **kw)
        data["lang_source"] = "chat_member" if (self.prefer_chat_member and raw) else "tele"

        try:
            if user and int(user.id) != int(OWNER_ID):
                set_lang(user.id, chosen)
        except Exception:
            logger.exception("[LanguageMW:db] sync error")

        return await handler(event, data)
