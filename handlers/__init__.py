from aiogram import Router

from handlers.bot.finder import router as finder_router
from handlers.bot.owner import router as owner_router

routers: list[Router] = [finder_router, owner_router]

__all__ = ['routers']
