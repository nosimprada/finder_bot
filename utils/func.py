from datetime import date


def _calc_age_years(birth_year: int) -> int:
    return max(0, int(date.today().year) - int(birth_year))

def _extract_start_arg(text: str | None) -> str:
    if not text:
        return ""
    parts = text.strip().split(maxsplit=1)
    return parts[1].strip() if len(parts) == 2 else ""

def _pick_lang(code: str | None) -> str:
    if not code:
        return "ru"  

    code = code.strip().replace("_", "-").lower()

    # алиасы/устаревшие коды Telegram
    alias = {
        "iw": "he",  # иврит
        "in": "id",  # индонезийский
        "ua": "uk",  # иногда встречается как 'ua'
    }
    code = alias.get(code, code)

    # zh-* -> zh (упрощаем)
    if code.startswith("zh-"):
        return "zh"

    # убираем региональную часть
    base = code.split("-", 1)[0]
    return base or "ru"

def _select_time_text(lang: str, minutes: int) -> str:
    code = (lang or "").lower()

    # Русский
    if code.startswith("ru"):
        n = minutes % 100
        if 11 <= n <= 14:
            word = "минут"
        else:
            n = minutes % 10
            if n == 1:
                word = "минута"
            elif 2 <= n <= 4:
                word = "минуты"
            else:
                word = "минут"
        return f"{minutes} {word}"

    # Украинский (учтён алиас 'ua')
    if code.startswith("uk") or code.startswith("ua"):
        n = minutes % 100
        if 11 <= n <= 14:
            word = "хвилин"
        else:
            n = minutes % 10
            if n == 1:
                word = "хвилина"
            elif 2 <= n <= 4:
                word = "хвилини"
            else:
                word = "хвилин"
        return f"{minutes} {word}"

    # По умолчанию — английский
    return f"{minutes} {'minute' if minutes == 1 else 'minutes'}"