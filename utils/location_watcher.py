from __future__ import annotations

import asyncio
import math
import time
from dataclasses import dataclass
from typing import Dict, Tuple, Optional

from aiogram import Bot

from config import OWNER_LANG, get_owner_lang
from utils.i18n import I18N as _I18N, I18n
from utils.outbox import send_proximity_notification

@dataclass
class LivePoint:
    lat: float
    lon: float
    live_until: float  

_locations_owner: Dict[int, LivePoint] = {}
_locations_finder: Dict[int, LivePoint] = {}
_watch_tasks: Dict[Tuple[int, int], asyncio.Task] = {}

_missing_notified: Dict[Tuple[int, int, str], bool] = {}


def _haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371000.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlmb = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlmb/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


def set_owner_live(owner_id: int, lat: float, lon: float, live_period_sec: int) -> None:
    _locations_owner[owner_id] = LivePoint(lat=lat, lon=lon, live_until=time.time() + int(live_period_sec))
    # сбрасываем «напоминание владельцу» для всех пар с этим owner
    for key in list(_missing_notified.keys()):
        o_id, _, side = key
        if o_id == owner_id and side == "owner":
            _missing_notified.pop(key, None)
    print(f"[WATCHER][OWNER] owner_id={owner_id} live set: "
          f"lat={lat:.6f} lon={lon:.6f} period={int(live_period_sec)}s "
          f"until={int(_locations_owner[owner_id].live_until)}")


def set_finder_live(finder_id: int, lat: float, lon: float, live_period_sec: int) -> None:
    _locations_finder[finder_id] = LivePoint(lat=lat, lon=lon, live_until=time.time() + int(live_period_sec))
    # сбрасываем «напоминание нашедшему» для всех пар с этим finder
    for key in list(_missing_notified.keys()):
        _, f_id, side = key
        if f_id == finder_id and side == "finder":
            _missing_notified.pop(key, None)
    print(f"[WATCHER][FINDER] finder_id={finder_id} live set: "
          f"lat={lat:.6f} lon={lon:.6f} period={int(live_period_sec)}s "
          f"until={int(_locations_finder[finder_id].live_until)}")


def clear_pair(owner_id: int, finder_id: int) -> None:
    print(f"[WATCHER] clear_pair for (owner={owner_id}, finder={finder_id})")
    _locations_owner.pop(owner_id, None)
    _locations_finder.pop(finder_id, None)
    _missing_notified.pop((owner_id, finder_id, "owner"), None)
    _missing_notified.pop((owner_id, finder_id, "finder"), None)
    task = _watch_tasks.pop((owner_id, finder_id), None)
    if task and not task.done():
        print(f"[WATCHER] cancel running task for pair (owner={owner_id}, finder={finder_id})")
        task.cancel()


def ensure_watcher_for_pair(
    bot: Bot,
    owner_id: int,
    finder_id: int,
    finder_lang: str,
    owner_lang: Optional[str] = None,   # ⬅ было: owner_lang: str = get_owner_lang()
    i18n: Optional[I18n] = None,
    distance_threshold_m: int = 20,
    poll_interval_sec: float = 3.0,
    test_force_close_after_sec: Optional[float] = None,  # ⬅ можно оставить — по умолчанию None
) -> None:
    if owner_id not in _locations_owner:
        print(f"[WATCHER] owner live not set yet → watcher NOT started (owner={owner_id}, finder={finder_id})")
        return

    key = (owner_id, finder_id)
    if key in _watch_tasks and not _watch_tasks[key].done():
        print(f"[WATCHER] already running for pair (owner={owner_id}, finder={finder_id})")
        return

    i18n = i18n or _I18N
    owner_lang = owner_lang or get_owner_lang()  # ⬅ подхватить актуальный язык
    print(f"[WATCHER] starting for pair (owner={owner_id}, finder={finder_id}) "
          f"threshold={distance_threshold_m}m poll={poll_interval_sec}s"
          + (f" [TEST force in {test_force_close_after_sec}s]" if test_force_close_after_sec else ""))

    started_at = time.time()

    async def _watch_loop() -> None:
        try:
            while True:
                await asyncio.sleep(poll_interval_sec)

                # ⬇ тестовый шорткат сработает только если ты его явно передашь (в проде его нет)
                if test_force_close_after_sec is not None and (time.time() - started_at) >= test_force_close_after_sec:
                    print(f"[WATCHER][TEST] force-close after {test_force_close_after_sec}s → notify & stop")
                    await _notify_both_close(bot, owner_id, finder_id, owner_lang, finder_lang, i18n)
                    clear_pair(owner_id, finder_id)
                    return

                now = time.time()
                owner_pt = _locations_owner.get(owner_id)
                finder_pt = _locations_finder.get(finder_id)

                if not owner_pt and not finder_pt:
                    print(f"[WATCHER] pair (owner={owner_id}, finder={finder_id}) no points yet — waiting")
                    continue

                # истёкшая/отсутствующая live → одноразовые репромпты
                if not owner_pt or owner_pt.live_until < now:
                    await _maybe_reprompt_owner_once(bot, owner_id, finder_id, owner_lang, i18n)
                    if owner_pt:
                        print(f"[WATCHER] owner live expired for owner={owner_id} (until={int(owner_pt.live_until)})")
                    _locations_owner.pop(owner_id, None)

                if not finder_pt or finder_pt.live_until < now:
                    await _maybe_reprompt_finder_once(bot, owner_id, finder_id, finder_lang, i18n)
                    if finder_pt:
                        print(f"[WATCHER] finder live expired for finder={finder_id} (until={int(finder_pt.live_until)})")
                    _locations_finder.pop(finder_id, None)

                # нужны обе актуальные точки
                owner_pt = _locations_owner.get(owner_id)
                finder_pt = _locations_finder.get(finder_id)
                if not owner_pt or not finder_pt:
                    continue

                # расстояние по Haversine
                dist_m = _haversine_m(owner_pt.lat, owner_pt.lon, finder_pt.lat, finder_pt.lon)
                print(f"[WATCHER] distance(owner={owner_id}, finder={finder_id}) = {dist_m:.2f} m")

                if dist_m <= distance_threshold_m:
                    print(f"[WATCHER] pair (owner={owner_id}, finder={finder_id}) reached threshold ({dist_m:.2f} m) → notify & stop")
                    await _notify_both_close(bot, owner_id, finder_id, owner_lang, finder_lang, i18n)
                    clear_pair(owner_id, finder_id)
                    return
        except asyncio.CancelledError:
            print(f"[WATCHER] cancelled for pair (owner={owner_id}, finder={finder_id})")
            return
        except Exception as e:
            print(f"[WATCHER][ERROR] pair (owner={owner_id}, finder={finder_id}) loop crashed: {e}")
            return

    _watch_tasks[key] = asyncio.create_task(_watch_loop())
    print(f"[WATCHER] task created for pair (owner={owner_id}, finder={finder_id})")


async def _notify_both_close(bot: Bot, owner_id: int, finder_id: int, owner_lang: str, finder_lang: str, i18n: I18n) -> None:
    print(f"[WATCHER] notify both close for pair (owner={owner_id}, finder={finder_id})")
    try:
        await send_proximity_notification(bot, owner_id, owner_lang, i18n)
    except Exception as e:
        print(f"[WATCHER][WARN] failed to notify owner {owner_id}: {e}")
    try:
        await send_proximity_notification(bot, finder_id, finder_lang, i18n)
    except Exception as e:
        print(f"[WATCHER][WARN] failed to notify finder {finder_id}: {e}")



#одноразовые репромпты

async def _maybe_reprompt_owner_once(bot: Bot, owner_id: int, finder_id: int, owner_lang: str, i18n: I18n) -> None:
    key = (owner_id, finder_id, "owner")
    if _missing_notified.get(key):
        return
    _missing_notified[key] = True
    print(f"[WATCHER] reprompt OWNER (once) for (owner={owner_id}, finder={finder_id})")
    try:
        await bot.send_message(owner_id, i18n.t(owner_lang, "alert_eror_location"))
    except Exception as e:
        print(f"[WATCHER][WARN] failed to notify owner {owner_id}: {e}")


async def _maybe_reprompt_finder_once(bot: Bot, owner_id: int, finder_id: int, finder_lang: str, i18n: I18n) -> None:
    key = (owner_id, finder_id, "finder")
    if _missing_notified.get(key):
        return
    _missing_notified[key] = True
    print(f"[WATCHER] reprompt FINDER (once) for (owner={owner_id}, finder={finder_id})")
    try:
        await bot.send_message(finder_id, i18n.t(finder_lang, "alert_eror_location"))
    except Exception as e:
        print(f"[WATCHER][WARN] failed to notify finder {finder_id}: {e}")

def get_finder_point(finder_id: int) -> Optional[LivePoint]:
    return _locations_finder.get(finder_id)

def get_owner_point(owner_id: int) -> Optional[LivePoint]:
    return _locations_owner.get(owner_id)