from __future__ import annotations

from typing import Callable, Dict, Any, Awaitable, Optional, Iterable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
import logging
import re

from utils.i18n import I18N
from utils.finder_store import get_finder, set_lang
from config import OWNER_ID

logger = logging.getLogger("lang_middleware")


def _detect_supported_langs() -> Iterable[str]:
    for attr in ("locales", "LANGS", "languages", "available"):
        val = getattr(I18N, attr, None)
        if isinstance(val, dict):
            return tuple(val.keys())
        if isinstance(val, (list, tuple, set)):
            return tuple(val)
    return ("ru", "en")


class LanguageMiddleware(BaseMiddleware):
    def __init__(self, default_lang: str = "en"):
        super().__init__()
        self.default_lang = default_lang
        self._supported = set(map(str.lower, _detect_supported_langs()))
        logger.info("[LanguageMW:init] default=%r supported=%s", self.default_lang, sorted(self._supported))

    def _resolve_lang(self, raw_lang: Optional[str]) -> str:
        code = (raw_lang or "").strip().lower()
        base = code.split("-", 1)[0] if code else ""
        if base in self._supported:
            return base
        if "en" in self._supported:
            return "en"
        if self.default_lang in self._supported:
            return self.default_lang
        return next(iter(self._supported)) if self._supported else self.default_lang

    def _extract_lang_from_start(self, event: Any) -> Optional[str]:
        text = None
        if isinstance(event, Message):
            text = event.text or event.caption or ""
        elif isinstance(event, CallbackQuery):
            text = ""
        else:
            text = getattr(event, "text", "") or ""

        if not text or not text.startswith("/start"):
            return None

        parts = text.strip().split(maxsplit=1)
        if len(parts) < 2:
            return None
        payload = parts[1].strip()

        m = re.search(r"(?:^|[\s|:_-])lang=([a-zA-Z-]+)(?:$|[\s|:_-])", payload, re.IGNORECASE)
        if m:
            cand = m.group(1).lower().split("-", 1)[0]
            if cand in self._supported:
                return cand

        tokens = re.split(r"[^a-zA-Z0-9-]+", payload)
        for tok in tokens:
            base = tok.lower().split("-", 1)[0]
            if base in self._supported:
                return base

        return None

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        if "t" in data and "lang" in data:
            return await handler(event, data)

        user = data.get("event_from_user")
        raw_lang: Optional[str] = (getattr(user, "language_code", None) or "").lower() if user else None

        hinted = self._extract_lang_from_start(event)

        db_lang: Optional[str] = None
        row = None
        if user and int(getattr(user, "id", 0) or 0) != int(OWNER_ID):
            row = get_finder(user.id)
            db_lang = (row or {}).get("lang")

        detected = self._resolve_lang(raw_lang)

        chosen = hinted or (db_lang if db_lang in self._supported else None) or detected

        data["lang"] = chosen
        data["t"] = lambda key, **kw: I18N.t(chosen, key, **kw)
        data["lang_source"] = "hint" if hinted else ("db" if db_lang in self._supported else "tele")

        logger.info(
            "[LanguageMW:event] user=%s raw=%r hinted=%r db=%r chosen=%r source=%s",
            getattr(user, "id", None), raw_lang, hinted, db_lang, chosen, data["lang_source"]
        )

        try:
            if user and int(user.id) != int(OWNER_ID) and row is not None:
                if (db_lang or "").lower() != (chosen or "").lower():
                    set_lang(user.id, chosen)
                    logger.info("[LanguageMW:db] update lang: user=%s %r -> %r", user.id, db_lang, chosen)
        except Exception as e:
            logger.exception("[LanguageMW:db] sync error: %s", e)

        return await handler(event, data)
