from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text

from fetch.database import Database

db_connection = Database()


router = Router()


def categories_reply():
    message = ' 🧑🏼‍🍳  **Categories** 📋\n'

    categories = db_connection.categories()

    for index, category in enumerate(categories):
        message += f'    {index + 1}. {category};\n'

    return message


@router.message(Text('Categories'))
async def categories(
        message: Message
    ):

    message_reply = categories_reply()

    await message.answer(
        message_reply
    )
