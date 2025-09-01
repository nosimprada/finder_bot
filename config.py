from enum import IntEnum


BOT_TOKEN = "7680162257:AAFiccfuZXBoUqq0aIaiNFdQqD-D5sOz9x0"        
OWNER_ID = 7463989072  
OWNER_LANG = "ru"            
GROUP_CHAT_ID = -1001234567890   
GROUP_INVITE_LINK = "https://t.me/+xxxx"  

PET_NAME = "Барон"  
PET_BIRTH_YEAR = 2020

PET_PHOTO_PATH = "assets/photo.jpg"
ASSET_BEEP_AUDIO = "assets/beep.mp3"

SUPPORTED_LANGS = ("ru", "en", "es")  
DEFAULT_LANG = "en"

START_KEY = "7463989072"


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