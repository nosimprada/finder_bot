from __future__ import annotations
from typing import Dict, Optional, Tuple, List, Any, Union
from .db import get_conn, init_db
from config import Stage, STAGE_DEFAULT  

TG = Union[int, str]
StageLike = Union[int, Stage, None]

def _tg(tg_id: TG) -> str:
    return str(tg_id)

def _stage_to_int(stage: StageLike) -> int:
    """
    Нормализует stage -> int.
    None трактуем как STAGE_DEFAULT (обычно 0 = Stage.NONE).
    Поддерживает IntEnum и int.
    """
    if stage is None:
        return int(STAGE_DEFAULT)
    try:
        return int(stage)  # IntEnum/int
    except Exception:
        return int(STAGE_DEFAULT)

# ---------- базовые CRUD ----------

def ensure_finder(tg_id: TG, lang: Optional[str] = None, stage: StageLike = None) -> None:
    """
    Создаёт запись, если её нет. При наличии — опционально обновит lang и/или stage (число).
    Если stage=None, не трогаем этап (оставляем текущий/дефолтный).
    """
    init_db()
    with get_conn() as db:
        db.execute("INSERT OR IGNORE INTO finders(tg_id) VALUES(?)", (_tg(tg_id),))
        if lang is not None and stage is not None:
            db.execute(
                "UPDATE finders SET lang=?, stage=? WHERE tg_id=?",
                (lang, _stage_to_int(stage), _tg(tg_id)),
            )
        elif lang is not None:
            db.execute("UPDATE finders SET lang=? WHERE tg_id=?", (lang, _tg(tg_id)))
        elif stage is not None:
            db.execute("UPDATE finders SET stage=? WHERE tg_id=?", (_stage_to_int(stage), _tg(tg_id)))

def set_lang(tg_id: TG, lang: str) -> None:
    init_db()
    with get_conn() as db:
        db.execute(
            "INSERT INTO finders(tg_id, lang) VALUES(?, ?) "
            "ON CONFLICT(tg_id) DO UPDATE SET lang=excluded.lang",
            (_tg(tg_id), lang),
        )

def get_finder(tg_id: TG) -> Optional[Dict[str, Any]]:
    init_db()
    with get_conn() as db:
        row = db.execute(
            "SELECT tg_id, lang, queue, completed, blocked, stage FROM finders WHERE tg_id=?",
            (_tg(tg_id),),
        ).fetchone()
        if not row:
            return None
        d = dict(row)
        st = d.get("stage")
        d["stage"] = int(st) if st is not None else int(STAGE_DEFAULT)
        return d

# ---------- stage helpers ----------

def set_stage(tg_id: TG, stage: StageLike) -> None:
    """Установить текущий этап (число). Передай None, чтобы сбросить в STAGE_DEFAULT (0)."""
    init_db()
    with get_conn() as db:
        ensure_finder(tg_id)
        db.execute("UPDATE finders SET stage=? WHERE tg_id=?", (_stage_to_int(stage), _tg(tg_id)))

def get_stage(tg_id: TG) -> int:
    """Вернёт текущий этап как int. Если NULL в БД, вернёт STAGE_DEFAULT."""
    init_db()
    with get_conn() as db:
        row = db.execute("SELECT stage FROM finders WHERE tg_id=?", (_tg(tg_id),)).fetchone()
        if not row or row["stage"] is None:
            return int(STAGE_DEFAULT)
        return int(row["stage"])

def reset_stage(tg_id: TG) -> None:
    set_stage(tg_id, STAGE_DEFAULT)

def stage_is(tg_id: TG, *stages: StageLike) -> bool:
    """
    Предикат: совпадает ли текущий этап с любым из указанных.
    Пример: stage_is(tg, Stage.FINDER_ETA_MENU, Stage.SOUND_PLAYING)
    """
    cur = get_stage(tg_id)
    ints = { _stage_to_int(x) for x in stages if x is not None }
    return cur in ints



def _max_queue(db) -> int:
    row = db.execute("SELECT MAX(queue) AS m FROM finders WHERE queue IS NOT NULL").fetchone()
    return int(row["m"]) if row and row["m"] is not None else 0

def _queue_pos(db, tg_id: TG) -> Optional[int]:
    row = db.execute("SELECT queue FROM finders WHERE tg_id=?", (_tg(tg_id),)).fetchone()
    if not row:
        return None
    q = row["queue"]
    return int(q) if q is not None else None

def _shift_after(db, removed_pos: int) -> None:
    db.execute(
        "UPDATE finders SET queue = queue - 1 "
        "WHERE queue IS NOT NULL AND queue > ?",
        (removed_pos,),
    )

# ---------- статус ----------

def status_of(tg_id: TG) -> Tuple[str, Optional[int]]:
    """
    ('blocked', None) | ('completed', None) | ('active', None) | ('queued', pos:int) | ('none', None)
    """
    init_db()
    with get_conn() as db:
        row = db.execute(
            "SELECT queue, completed, blocked FROM finders WHERE tg_id=?",
            (_tg(tg_id),),
        ).fetchone()
        if not row:
            return "none", None
        if row["blocked"]:
            return "blocked", None
        if row["completed"]:
            return "completed", None
        q = row["queue"]
        if q is None:
            return "none", None
        q = int(q)
        if q == 1:
            return "active", None
        return "queued", q

def status_and_stage(tg_id: TG) -> Tuple[str, Optional[int], int]:
    """Статус + текущий числовой этап (никогда не None, минимум 0)."""
    st, pos = status_of(tg_id)
    return st, pos, get_stage(tg_id)

def get_active() -> Optional[str]:
    init_db()
    with get_conn() as db:
        row = db.execute("SELECT tg_id FROM finders WHERE queue = 1").fetchone()
        return row["tg_id"] if row else None

def list_queue() -> List[str]:
    init_db()
    with get_conn() as db:
        rows = db.execute(
            "SELECT tg_id FROM finders WHERE queue IS NOT NULL ORDER BY queue"
        ).fetchall()
        return [r["tg_id"] for r in rows]

def queue_positions() -> Dict[str, int]:
    init_db()
    with get_conn() as db:
        rows = db.execute(
            "SELECT tg_id, queue FROM finders WHERE queue IS NOT NULL ORDER BY queue"
        ).fetchall()
        return {r["tg_id"]: int(r["queue"]) for r in rows}

# ---------- действия ----------

def enqueue(tg_id: TG, lang: Optional[str] = None) -> int:
    """
    Поставить в очередь. Возвращает позицию (1..N).
    """
    init_db()
    with get_conn() as db:
        ensure_finder(tg_id, lang=lang)
        row = db.execute("SELECT blocked FROM finders WHERE tg_id=?", (_tg(tg_id),)).fetchone()
        if row and row["blocked"]:
            raise RuntimeError("user_is_blocked")

        pos = _queue_pos(db, tg_id)
        if pos is not None:
            return pos

        mx = _max_queue(db)
        if mx == 0:
            db.execute("UPDATE finders SET queue=1, completed=0 WHERE tg_id=?", (_tg(tg_id),))
            return 1

        new_pos = mx + 1
        db.execute("UPDATE finders SET queue=?, completed=0 WHERE tg_id=?", (new_pos, _tg(tg_id)))
        return new_pos

def promote_if_idle() -> Optional[str]:
    """
    Если нет активного (queue=1), но есть кто-то в очереди — сделать минимального активным.
    """
    init_db()
    with get_conn() as db:
        row = db.execute("SELECT tg_id FROM finders WHERE queue = 1").fetchone()
        if row:
            return None
        row2 = db.execute(
            "SELECT tg_id FROM finders WHERE queue IS NOT NULL ORDER BY queue LIMIT 1"
        ).fetchone()
        if not row2:
            return None
        db.execute("UPDATE finders SET queue=1 WHERE tg_id=?", (row2["tg_id"],))
        return row2["tg_id"]

def finish_active(mark_completed: bool = True) -> Optional[str]:
    """
    Завершить текущего активного и продвинуть очередь.
    stage всегда сбрасывается в STAGE_DEFAULT (0).
    """
    init_db()
    with get_conn() as db:
        row = db.execute("SELECT tg_id FROM finders WHERE queue = 1").fetchone()
        if row:
            tg = row["tg_id"]
            if mark_completed:
                db.execute(
                    "UPDATE finders SET completed=1, queue=NULL, stage=? WHERE tg_id=?",
                    (int(STAGE_DEFAULT), tg),
                )
            else:
                db.execute(
                    "UPDATE finders SET queue=NULL, stage=? WHERE tg_id=?",
                    (int(STAGE_DEFAULT), tg),
                )
            _shift_after(db, 1)

        row2 = db.execute("SELECT tg_id FROM finders WHERE queue = 1").fetchone()
        return row2["tg_id"] if row2 else None

def remove_from_queue(tg_id: TG) -> bool:
    """Убрать из очереди (если был). Этап не меняем."""
    init_db()
    with get_conn() as db:
        pos = _queue_pos(db, tg_id)
        if pos is None:
            return False
        db.execute("UPDATE finders SET queue=NULL WHERE tg_id=?", (_tg(tg_id),))
        _shift_after(db, pos)
        return True

def block_user(tg_id: TG) -> None:
    """
    Заблокировать пользователя:
      - убрать из очереди и сдвинуть хвост;
      - blocked=1, completed=0, stage=STAGE_DEFAULT (0).
    """
    init_db()
    with get_conn() as db:
        pos = _queue_pos(db, tg_id)
        if pos is not None:
            db.execute("UPDATE finders SET queue=NULL WHERE tg_id=?", (_tg(tg_id),))
            _shift_after(db, pos)
        db.execute(
            "UPDATE finders SET blocked=1, completed=0, stage=? WHERE tg_id=?",
            (int(STAGE_DEFAULT), _tg(tg_id)),
        )

def unblock_user(tg_id: TG, lang: Optional[str] = None) -> int:
    init_db()
    with get_conn() as db:
        ensure_finder(tg_id, lang=lang)
        db.execute("UPDATE finders SET blocked=0 WHERE tg_id=?", (_tg(tg_id),))
        pos = _queue_pos(db, tg_id)
        if pos is not None:
            return pos
        new_pos = _max_queue(db) + 1
        db.execute("UPDATE finders SET queue=?, completed=0 WHERE tg_id=?", (new_pos, _tg(tg_id)))
        return new_pos

def reset_completed(tg_id: TG) -> None:
    init_db()
    with get_conn() as db:
        db.execute("UPDATE finders SET completed=0 WHERE tg_id=?", (_tg(tg_id),))

def clear_all() -> None:
    init_db()
    with get_conn() as db:
        db.execute("DELETE FROM finders")
