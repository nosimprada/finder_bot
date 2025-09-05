from __future__ import annotations
from typing import Optional
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from utils.i18n import I18N as _I18N, I18n


def _i18n(i18n: Optional[I18n]) -> I18n:
    return i18n or _I18N


#finder

def kb_finder_welcome(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "contact_owner"), callback_data="finder:contact_owner")
    kb.adjust(1)
    return kb.as_markup()

def kb_finder_share_location(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "share_location"), callback_data="finder:share_location")
    kb.adjust(1)
    return kb.as_markup()

def kb_owner_share_location(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "share_location"), callback_data="owner:share_location")
    kb.adjust(1)
    return kb.as_markup()


#owner

def kb_owner_contact(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "contact_action"), callback_data="owner:contact")
    kb.adjust(1)
    return kb.as_markup()


def kb_owner_request_only(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "request_pet_location"), callback_data="owner:ask_location")
    kb.adjust(1)
    return kb.as_markup()


def kb_owner_arrival_menu(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "arrive_10"), callback_data="owner:eta:10")
    kb.button(text=i18n.t(lang, "arrive_20"), callback_data="owner:eta:20")
    kb.button(text=i18n.t(lang, "arrive_30"), callback_data="owner:eta:30")
    kb.button(text=i18n.t(lang, "arrive_60"), callback_data="owner:eta:1h")
    kb.button(text=i18n.t(lang, "check_finder_location"), callback_data="sound:check_finder")
    kb.button(text=i18n.t(lang, "start_chat"), callback_data="owner:start_chat")
    kb.adjust(1)  
    return kb.as_markup()


def kb_owner_chat_consent(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "accept_chat"), callback_data="owner:chat_accept")
    kb.button(text=i18n.t(lang, "back"),         callback_data="owner:chat_back")
    kb.adjust(1)
    return kb.as_markup()

def kb_open_group_link(lang: str, url: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "open_chat"), url=url)
    kb.adjust(1)
    return kb.as_markup()

def kb_sound_password(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "sound_password"), callback_data="sound:password")
    kb.adjust(1)
    return kb.as_markup()

def kb_sound_followup_owner(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "mission_done"), callback_data="sound:done")
    kb.adjust(1)
    return kb.as_markup()


def kb_sound_followup_finder(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "mission_done"), callback_data="sound:done")
    kb.adjust(1)
    return kb.as_markup()