from __future__ import annotations
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from typing import Optional
from utils.i18n import I18N as _I18N, I18n

def _i18n(i18n: Optional[I18n]) -> I18n:
    return i18n or _I18N


def kb_finder_welcome(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "contact_owner"), callback_data="finder:contact_owner")
    kb.adjust(1)
    return kb.as_markup()

def kb_user_show_location(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "show_location"), callback_data="user:show_location")
    kb.adjust(1)
    return kb.as_markup()

def kb_finder_eta_menu(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "arrive_10"), callback_data="finder:eta:10")
    kb.button(text=i18n.t(lang, "arrive_20"), callback_data="finder:eta:20")
    kb.button(text=i18n.t(lang, "arrive_30"), callback_data="finder:eta:30")
    kb.button(text=i18n.t(lang, "cannot_arrive"), callback_data="finder:cant_come")
    kb.adjust(2, 2)
    return kb.as_markup()

def kb_finder_share_location(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "share_location"), callback_data="finder:share_location")
    kb.adjust(1)
    return kb.as_markup()

#OWNER

def kb_owner_contact(lang: str, finder_id: int, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "contact_action"), callback_data=f"owner:contact:{finder_id}")
    kb.adjust(1)
    return kb.as_markup()

def kb_owner_action_menu(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "send_my_location"), callback_data="owner:send_location")
    kb.button(text=i18n.t(lang, "request_pet_location"), callback_data="owner:ask_location")
    kb.adjust(1)
    return kb.as_markup()

def kb_owner_eta_menu(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "arrive_10"), callback_data="owner:eta:10")
    kb.button(text=i18n.t(lang, "arrive_20"), callback_data="owner:eta:20")
    kb.button(text=i18n.t(lang, "arrive_30"), callback_data="owner:eta:30")
    kb.button(text=i18n.t(lang, "start_chat"), callback_data="owner:start_chat")
    kb.adjust(2, 2)
    return kb.as_markup()

def kb_accept_language_mismatch(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "accept_chat"), callback_data="owner:accept_language_mismatch")
    kb.adjust(1)
    return kb.as_markup()

def kb_sound_password(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "sound_password"), callback_data="sound:play")
    kb.adjust(1)
    return kb.as_markup()

def kb_mission_menu(lang: str, i18n: Optional[I18n] = None) -> InlineKeyboardMarkup:
    i18n = _i18n(i18n)
    kb = InlineKeyboardBuilder()
    kb.button(text=i18n.t(lang, "mission_success"), callback_data="mission:done")
    kb.button(text=i18n.t(lang, "something_wrong"), callback_data="mission:check_owner_loc")
    kb.adjust(1, 1)
    return kb.as_markup()
