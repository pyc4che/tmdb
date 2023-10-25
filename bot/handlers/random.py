from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

from fetch.database import Database

router = Router()

db_connection = Database()


def random_reply():
    data = db_connection.random_meal()

    message = f'ID: {data[0][1]}\n\n'

    for element in data[1:]:
        message += f'{element[0]}: {element[1]}\n'

    return message


@router.message(Text('Random Meal'))
async def random_meal(message: Message):
    await message.answer(
        str(random_reply())
    )
