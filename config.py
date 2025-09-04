
from enum import IntEnum
from aiogram import Bot

#===============================================================
BOT_TOKEN = "7680162257:AAFiccfuZXBoUqq0aIaiNFdQqD-D5sOz9x0"        
OWNER_ID = 165612690  # 818235411 1443074332  7463989072   165612690   
GROUP_CHAT_ID = -1002997063260   
GROUP_INVITE_LINK = "https://t.me/+dweFD32KpRgyYWFi"  
START_KEY = "7463989072"
PET_NAME = "Барон"  
PET_BIRTH_YEAR = 2020
PET_PHOTO_PATH = "assets/photo.jpg"
#===============================================================





ASSET_BEEP_AUDIO = "assets/beep.mp3"

SUPPORTED_LANGS = ("ru", "en", "es")  
DEFAULT_LANG = "en"
INSTRUCTION_VIDEO_FILE_ID: str | None = None
SOUND_MP3_FILE_ID: str | None = None



OWNER_LANG: str = DEFAULT_LANG  # дефолт до первого

def _normalize_lang_any(code: str | None, fallback: str = DEFAULT_LANG) -> str:
    if not code:
        return fallback
    code = code.strip().replace("_", "-").lower()

    alias_map = {
        "iw": "he",  # Hebrew legacy
        "in": "id",  # Indonesian legacy
        "ua": "uk",  # иногда встречается
    }
    if code in alias_map:
        return alias_map[code]

    if code.startswith("zh-"):
        return "zh"

    base = code.split("-", 1)[0]
    return base or fallback


def get_owner_lang() -> str:
    return OWNER_LANG


async def refresh_owner_lang(bot: Bot) -> str:
    global OWNER_LANG
    try:
        cm = await bot.get_chat_member(chat_id=OWNER_ID, user_id=OWNER_ID)
        raw = getattr(cm.user, "language_code", None)
        OWNER_LANG = _normalize_lang_any(raw, DEFAULT_LANG)
        print(f"[config] OWNER_LANG set to {OWNER_LANG!r} from Telegram (raw={raw!r})")
    except Exception as e:
        print(f"[config] refresh_owner_lang failed: {e}. Keeping OWNER_LANG={OWNER_LANG!r}")
    return OWNER_LANG


async def owner_lang_autorefresh(bot: Bot, interval_sec: int = 1800) -> None:
    import asyncio
    while True:
        try:
            await refresh_owner_lang(bot)
        except Exception as e:
            print(f"[config] owner_lang_autorefresh error: {e}")
        await asyncio.sleep(interval_sec)

class Stage(IntEnum):
    # 0 — нет активного шага
    NONE = 0

    # 10–29: старт и приветствие
    START_SCREEN = 10                  # показана кнопка СТАРТ
    FINDER_WELCOME_SHOWN = 11          # карточка питомца показана (страница питомца)

    # 30–39: первичный контакт и меню владельца
    FINDER_PRESSED_CONTACT_OWNER = 20  # нашедший нажал «Связаться с владельцем»
    OWNER_CONTACT_PROMPT_SHOWN = 30    # у владельца показана карточка с кнопкой «Связаться»
    OWNER_ACTION_MENU = 31             # у владельца выведено меню «Отправить локацию / Узнать локацию»

    # 40–49: обмен локациями
    OWNER_SENT_LOCATION = 40           # владелец отправил live-локацию
    OWNER_REQUESTED_FINDER_LOCATION = 41 # владелец запросил локацию нашедшего
    THE_FINDER_WAS_SHOWN_INSTRUCTIONS_FOR_SENDING_THE_LOCATION = 43 # нашедший получил инструкцию по отправке локации
    FINDER_SHARED_LOCATION = 42        # нашедший отправил live-локацию

    # 50–59: ETA (когда прибуду)
    FINDER_ETA_MENU = 50               # у нашедшего открыт выбор ETA (10/20/30/нет возможности)
    OWNER_ETA_MENU = 51                # у владельца открыт выбор ETA
    FINDER_CANT_COME_WAITING = 52      # нашедший выбрал «не могу приехать, жду тут»

    # 70–79: навигационные подсказки
    NAV_HINT_SHOWN = 70                # подсказки «перейдите в режим навигации…»

    # 80–89: чат/язык/приглашение
    LANGUAGE_MISMATCH_WARNING = 80     # предупреждение о возможной разнице языков
    WAITING_CHAT_ACCEPT = 81           # показана кнопка «Принимаю»
    GROUP_INVITE_SENT = 82             # приглашение в группу отправлено

    # 90–99: близость/звук
    PROXIMITY_ALERTED = 90             # триггер близости (≈20м) от Telegram
    SOUND_PASSWORD_PROMPT = 91         # показана кнопка «Звуковой пароль»
    SOUND_PLAYING = 92                 # идёт воспроизведение звукового пароля

    # 100+: финал
    MISSION_MENU = 100                 # меню «Миссия выполнена / Проверить локацию…»
    COMPLETED = 200                    # сценарий завершён (для истории/метрик)

STAGE_DEFAULT = Stage.NONE

STAGE_LABELS = {s.value: s.name for s in Stage}