from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "storage" / "bot.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def _column_exists(db: sqlite3.Connection, table: str, column: str) -> bool:
    rows = db.execute(f"PRAGMA table_info({table})").fetchall()
    return any(r["name"] == column for r in rows)

def init_db() -> None:
    with get_conn() as db:
        db.executescript("""
        PRAGMA journal_mode=WAL;
        PRAGMA foreign_keys=ON;

        CREATE TABLE IF NOT EXISTS finders (
            tg_id     TEXT PRIMARY KEY,
            lang      TEXT,
            queue     INTEGER,                      -- NULL: вне очереди; 1: активный; 2..: очередь
            completed INTEGER NOT NULL DEFAULT 0,   -- 0/1
            blocked   INTEGER NOT NULL DEFAULT 0,   -- 0/1
            stage     INTEGER NOT NULL DEFAULT 0    -- текущий этап (число из config.Stage)
        );
        """)
        if not _column_exists(db, "finders", "stage"):
            db.execute("ALTER TABLE finders ADD COLUMN stage INTEGER")
            db.execute("UPDATE finders SET stage = 0 WHERE stage IS NULL")
