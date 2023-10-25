from aiogram import Router

from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message


router = Router()


def get_menu_reply_markup() -> ReplyKeyboardMarkup:

    buttons = [
        'Random Meal', 'Search by Name', 'Categories',
        'Search by Ingredient', 'Search By Category',
    ]

    builder = ReplyKeyboardBuilder()

    for button in buttons:
        builder.add(
            KeyboardButton(
                text=button
            )
        )
        builder.adjust(3)

    return builder.as_markup(
            resize_keyboard=True
        )


@router.message(Command(commands=['start']))
async def start(
        message: Message
    ):

    menu_markup = get_menu_reply_markup()

    await message.answer(
        "Hello, I'm TMDB Bot",
        reply_markup=menu_markup
    )
