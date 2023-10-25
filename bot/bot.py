from aiogram import Bot

from config.config import Config

token = Config(
    './configs/config.ini'
).read()

bot = Bot(token)

