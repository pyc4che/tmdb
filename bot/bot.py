from aiogram import Bot

from config.config import Config

token = Config(
    '../../configs/config.conf'
).read()

bot = Bot(token)
