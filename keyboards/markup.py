from __future__ import annotations
from typing import Optional
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from utils.i18n import I18N as _I18N, I18n


def _i18n(i18n: Optional[I18n]) -> I18n:
    return i18n or _I18N


# ----- finder side -----

def kb_finder_welcome(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "contact_owner"), callback_data="finder:contact_owner")
    kb.adjust(1)
    return kb.as_markup()

def kb_finder_share_location(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    """Кнопка для нашедшего «Поделиться локацией» (колбэк: finder:share_location)."""
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "share_location"), callback_data="finder:share_location")
    kb.adjust(1)
    return kb.as_markup()


# ----- owner side -----

def kb_owner_contact(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    """
    Кнопка «Связаться» для владельца — без привязки к finder_id.
    Колбэк: owner:contact
    """
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "contact_action"), callback_data="owner:contact")
    kb.adjust(1)
    return kb.as_markup()


def kb_owner_action_menu(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    """
    Меню действий владельца:
    - Отправить мою локацию → owner:send_location
    - Узнать локацию питомца → owner:ask_location
    """
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "send_my_location"), callback_data="owner:send_location")
    kb.button(text=i18n.t(lang, "request_pet_location"), callback_data="owner:ask_location")
    kb.adjust(1)
    return kb.as_markup()
