import asyncio

from aiogram import Dispatcher

from bot.bot import bot
from bot.handlers import router

from shared.logger import setup_loggers


async def main():
    dispatcher = Dispatcher()

    dispatcher.include_router(
        router
    )

    await dispatcher.start_polling(
        bot
    )


if __name__ == '__main__':
    setup_loggers()

    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        main()
    )
