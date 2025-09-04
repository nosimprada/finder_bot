from __future__ import annotations

CYRILLIC_LANGS = {"ru", "uk", "bg"}

def _norm_lang(lang: str | None) -> str:
    if not lang:
        return "en"
    return lang.split("-")[0].lower()

def ru_to_latin(text: str) -> str:
    """
    Приближённая транслитерация RU->LAT (в духе BGN/PCGN).
    Хватает для имён типа «Барон» -> «Baron».
    """
    table = {
        "А": "A",  "а": "a",
        "Б": "B",  "б": "b",
        "В": "V",  "в": "v",
        "Г": "G",  "г": "g",
        "Д": "D",  "д": "d",
        "Е": "E",  "е": "e",  # спец-правило 
        "Ё": "Yo", "ё": "yo",
        "Ж": "Zh", "ж": "zh",
        "З": "Z",  "з": "z",
        "И": "I",  "и": "i",
        "Й": "Y",  "й": "y",
        "К": "K",  "к": "k",
        "Л": "L",  "л": "l",
        "М": "M",  "м": "m",
        "Н": "N",  "н": "n",
        "О": "O",  "о": "o",
        "П": "P",  "п": "p",
        "Р": "R",  "р": "r",
        "С": "S",  "с": "s",
        "Т": "T",  "т": "t",
        "У": "U",  "у": "u",
        "Ф": "F",  "ф": "f",
        "Х": "Kh", "х": "kh",
        "Ц": "Ts", "ц": "ts",
        "Ч": "Ch", "ч": "ch",
        "Ш": "Sh", "ш": "sh",
        "Щ": "Shch","щ": "shch",
        "Ы": "Y",  "ы": "y",
        "Э": "E",  "э": "e",
        "Ю": "Yu", "ю": "yu",
        "Я": "Ya", "я": "ya",
        "Ь": "",   "ь": "",
        "Ъ": "",   "ъ": "",
    }

    vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
    res: list[str] = []
    prev = ""
    for i, ch in enumerate(text):
        if ch in ("Е", "е"):
            if i == 0 or prev in vowels or prev in ("ь", "Ь", "ъ", "Ъ"):
                res.append("Ye" if ch == "Е" else "ye")
            else:
                res.append("E" if ch == "Е" else "e")
        else:
            res.append(table.get(ch, ch))
        prev = ch
    return "".join(res)

def transliterate_pet_name(name_ru: str, lang: str | None) -> str:
    code = _norm_lang(lang)
    if code in CYRILLIC_LANGS:
        return name_ru
    return ru_to_latin(name_ru)
