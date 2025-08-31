from aiogram import Router

from handlers.bot.finder import router as finder_router

routers: list[Router] = [finder_router]

__all__ = ['routers']
