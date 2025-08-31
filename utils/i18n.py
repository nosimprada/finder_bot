from __future__ import annotations
from typing import Dict, Any

locales: Dict[str, Dict[str, str]] = {
    "ru": {
        "start_button": "СТАРТ",
        "start_chat": "Перейти в чат",
        "contact_owner": "Связаться с владельцем",
        "contact_action": "Связаться",
        "send_my_location": "Отправить мою локацию",
        "request_pet_location": "Узнать локацию питомца",
        "show_location": "Показать локацию",
        "arrive_10": "Прибуду в течение 10 минут",
        "arrive_20": "Прибуду в течение 20 минут",
        "arrive_30": "Прибуду в течение 30 минут",
        "share_location": "Поделиться локацией",
        "cannot_arrive": "Не могу приехать",
        "accept_chat": "Принимаю",
        "sound_password": "Звуковой пароль",
        "mission_success": "Миссия выполнена!",
        "something_wrong": "Что-то пошло не так? Проверить локацию питомца",
        "pet_info_message": (
            "Это страничка питомца: {pet_name}. Возраст питомца: {age} лет.\n\n"
            "Если вы читаете мою страницу, значит я потерялся. Я очень хочу домой, к своему хозяину. "
            "Он очень любит меня и скучает.\n"
            "Пожалуйста, свяжитесь с ним по кнопке ниже и помогите мне вернуться домой."
        ),
        "owner_alerted": "Владелец оповещён, сейчас он отреагирует.",
        "owner_found_pet": "Здравствуйте! Я нашёл вашего питомца, свяжитесь со мной, и я с радостью его вам верну.",
        "location_instruction": "Запросите локацию собеседника или поделитесь своей, чтобы встретиться",
        "owner_location_sent": (
            "Локация отправлена, не отходите далеко от неё до встречи с собеседником.\n"
            "Когда вы окажетесь рядом, получите оповещение."
        ),
        "user_location_sent": (
            "Я сейчас нахожусь здесь. Если вы недалеко и вам удобно, давайте встретимся в этой точке.\n"
            "Если вам удобнее, чтобы я прибыл к вам — отправьте свою локацию."
        ),
        "navigation_hint_owner": (
            "Перейдите в режим навигации, чтобы оценить время в пути, "
            "после чего сообщите время прибытия нашедшему питомца."
        ),
        "navigation_hint_user": (
            "Сообщите, когда вы прибудете. Сообщив время прибытия, вы также отправите свою локацию."
        ),
        "arrival_owner_10": "Прибуду в течение 10 минут, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_owner_20": "Прибуду в течение 20 минут, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_owner_30": "Прибуду в течение 30 минут, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_timer_warning": (
            "Вы должны прибыть к указанной точке в выбранный промежуток времени.\n"
            "Если вы опаздываете, обновите время прибытия через это меню."
        ),
        "cannot_arrive_waiting": "Не могу приехать: нахожусь в этой локации и буду ждать вас здесь.",
        "location_shared_response": (
            "Локация отправлена, ожидайте ответа. Не отходите далеко — получите оповещение при приближении."
        ),
        "navigation_to_user": (
            "Перейдите в режим навигации, чтобы оценить время в пути, "
            "после чего сообщите время прибытия нашедшему питомца."
        ),
        "final_meet_instruction": (
            "Сообщите, когда вы прибудете, или пригласите собеседника в чат для обсуждения."
        ),
        "language_warning": "Внимание! Язык общения собеседника может отличаться от вашего.",
        "location_requested": "Локация запрошена, ожидайте ответа.",
        "you_are_close": "Вы находитесь рядом! Включите звуковой пароль, оглянитесь и найдите друг друга.",
        "play_sound_caption": "Проигрывается звуковой пароль... Пожалуйста, оглянитесь вокруг!",
        "invite_text": "Перейдите по ссылке {invite_link}, чтобы продолжить общение в группе {group_name}.",
    },
    "en": {
        "start_button": "START",
        "start_chat": "Go to chat",
        "contact_owner": "Contact the owner",
        "contact_action": "Contact",
        "send_my_location": "Send my location",
        "request_pet_location": "Request pet location",
        "show_location": "Show location",
        "arrive_10": "Arrive within 10 minutes",
        "arrive_20": "Arrive within 20 minutes",
        "arrive_30": "Arrive within 30 minutes",
        "share_location": "Share location",
        "cannot_arrive": "Cannot arrive",
        "accept_chat": "Accept",
        "sound_password": "Sound password",
        "mission_success": "Mission accomplished!",
        "something_wrong": "Something went wrong? Check the pet's location",
        "pet_info_message": (
            "This is the page of the pet: {pet_name}. The pet is {age} years old.\n\n"
            "If you are reading my page, it means I am lost. I really want to go home to my owner. "
            "He loves me very much and misses me.\n"
            "Please contact him using the button below and help me return home."
        ),
        "owner_alerted": "The owner has been alerted, he will respond shortly.",
        "owner_found_pet": "Hello! I found your pet, please contact me and I will gladly return him to you.",
        "location_instruction": "Request the location of the other person or share yours to meet",
        "owner_location_sent": (
            "Location sent, do not go far from it until you meet the person.\n"
            "When you are close, you will receive a notification."
        ),
        "user_location_sent": (
            "I am here now. If you are nearby and it is convenient, let's meet at this point.\n"
            "If it is more convenient for you that I come to you — please send your location."
        ),
        "navigation_hint_owner": (
            "Switch to navigation mode to estimate travel time, "
            "then inform the pet finder of your arrival time."
        ),
        "navigation_hint_user": (
            "Inform when you will arrive. By informing the arrival time, you also send your location."
        ),
        "arrival_owner_10": "I will arrive within 10 minutes, please wait for me at your location point.",
        "arrival_owner_20": "I will arrive within 20 minutes, please wait for me at your location point.",
        "arrival_owner_30": "I will arrive within 30 minutes, please wait for me at your location point.",
        "arrival_timer_warning": (
            "You must arrive at the specified point within the chosen time frame.\n"
            "If you are late, update your arrival time through this menu."
        ),
        "cannot_arrive_waiting": "Cannot arrive: I am at this location and will wait for you here.",
        "location_shared_response": (
            "Location sent, please wait for a response. Do not go far — you will be notified when close."
        ),
        "navigation_to_user": (
            "Switch to navigation mode to estimate travel time, "
            "then inform the pet finder of your arrival time."
        ),
        "final_meet_instruction": (
            "Inform when you will arrive or invite the other person to chat to discuss."
        ),
        "language_warning": "Attention! The other person's communication language may differ from yours.",
        "location_requested": "Location requested, please wait for a response.",
        "you_are_close": "You are nearby! Turn on the sound password, look around and find each other.",
        "play_sound_caption": "The sound password is playing... Please look around!",
        "invite_text": "Follow the link {invite_link} to continue the conversation in the group {group_name}.",
    },
}

DEFAULT_LANG = "en"

def normalize_lang(lang: str | None) -> str:
    if not lang:
        return DEFAULT_LANG
    base = lang.split("-")[0].lower()
    return base if base in locales else DEFAULT_LANG

class I18n:
    def __init__(self, data: Dict[str, Dict[str, str]], default: str = DEFAULT_LANG):
        self.data = data
        self.default = default

    def t(self, lang: str, key: str, **kwargs: Any) -> str:
        code = normalize_lang(lang)
        bucket = self.data.get(code, {})
        s = bucket.get(key) or self.data[self.default].get(key) or key
        try:
            return s.format(**kwargs)
        except Exception:
            return s

I18N = I18n(locales, DEFAULT_LANG)
