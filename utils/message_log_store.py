from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any, List
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.enums import ChatType

STORE_PATH = Path(__file__).resolve().parents[1] / "storage" / "message_log.json"
STORE_PATH.parent.mkdir(parents=True, exist_ok=True)

def _load() -> Dict[str, Any]:
    if STORE_PATH.is_file():
        try:
            with STORE_PATH.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    return {"chats": {}}
                data.setdefault("chats", {})
                return data
        except Exception:
            return {"chats": {}}
    return {"chats": {}}

def _save(data: Dict[str, Any]) -> None:
    tmp = STORE_PATH.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(STORE_PATH)

def _ensure_chat(data: Dict[str, Any], chat_id: str) -> Dict[str, List[int]]:
    chats = data.setdefault("chats", {})
    chat = chats.setdefault(chat_id, {})
    chat.setdefault("bot", [])
    chat.setdefault("user", [])
    return chat

def _append_unique(seq: List[int], mid: int) -> None:
    if mid not in seq:
        seq.append(mid)

def log_user_message(chat_id: int | str, message_id: int) -> None:
    data = _load()
    chat = _ensure_chat(data, str(chat_id))
    _append_unique(chat["user"], int(message_id))
    _save(data)

def log_bot_message(chat_id: int | str, message_id: int) -> None:
    data = _load()
    chat = _ensure_chat(data, str(chat_id))
    _append_unique(chat["bot"], int(message_id))
    _save(data)

def get_chat_messages(chat_id: int | str) -> Dict[str, List[int]]:
    data = _load()
    chat = _ensure_chat(data, str(chat_id))
    return {"bot": list(chat["bot"]), "user": list(chat["user"])}

def clear_chat(chat_id: int | str) -> None:
    data = _load()
    data.setdefault("chats", {})[str(chat_id)] = {"bot": [], "user": []}
    _save(data)

def clear_all() -> None:
    _save({"chats": {}})

async def delete_logged_bot_messages(bot: Bot, chat_id: int | str) -> int:
    """
    Удаляет все сообщения БОТА, записанные для чата.
    Работает в личках и группах (если у бота есть права на удаление).
    Возвращает количество успешно удалённых.
    """
    data = _load()
    chat = _ensure_chat(data, str(chat_id))
    bot_ids = list(dict.fromkeys(chat.get("bot", [])))  
    ok = 0
    for mid in bot_ids:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=mid)
            ok += 1
        except (TelegramBadRequest, TelegramForbiddenError):
            pass
        except Exception:
            pass
    chat["bot"] = []
    _save(data)
    return ok

async def _get_chat_type(bot: Bot, chat_id: int | str) -> str | None:
    try:
        ch = await bot.get_chat(chat_id)
        ctype = getattr(ch, "type", None)
        if ctype == ChatType.PRIVATE or str(ctype).lower() == "chattype.private":
            return "private"
        return str(ctype) if ctype is not None else None
    except Exception:
        return None

async def delete_logged_user_messages(bot: Bot, chat_id: int | str) -> int:
    data = _load()
    chat = _ensure_chat(data, str(chat_id))
    user_ids = list(dict.fromkeys(chat.get("user", [])))
    ok = 0
    still_exists: List[int] = []

    chat_type = await _get_chat_type(bot, chat_id)
    is_private = (chat_type == "private")

    for mid in user_ids:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=mid)
            print(f'Пытаюсь удалить: {mid}')
            ok += 1
        except TelegramBadRequest as e:
            if is_private:
                pass
            else:
                desc = str(e)
                if "not found" in desc.lower():
                    pass
                else:
                    still_exists.append(mid)
        except TelegramForbiddenError:
            if is_private:
                pass
            else:
                still_exists.append(mid)
        except Exception:
            if is_private:
                pass
            else:
                still_exists.append(mid)

    chat["user"] = still_exists
    _save(data)
    return ok

async def delete_all_logged_messages(bot: Bot, chat_id: int | str) -> dict:
    deleted_bot = await delete_logged_bot_messages(bot, chat_id)
    deleted_user = await delete_logged_user_messages(bot, chat_id)
    return {"bot": deleted_bot, "user": deleted_user}
