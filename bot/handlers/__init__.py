from aiogram import Router

from bot.handlers.start import router as start_router
from bot.handlers.categories import router as categories_router


router = Router()

router.include_routers(
    start_router, categories_router
)
