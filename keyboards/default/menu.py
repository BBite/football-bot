from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, User

from loader import _
from utils.db_api import db

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_('Меню')),
            # KeyboardButton(text='Ігра')
        ],
        [
            KeyboardButton(text=_('Змінити мову'))
        ]
    ],
    resize_keyboard=True
)


def get_main_menu(lang: str) -> ReplyKeyboardMarkup:
    main_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('Меню', locale=lang)),
                # KeyboardButton(text='Ігра')
            ],
            [
                KeyboardButton(text=_('Змінити мову', locale=lang))
            ]
        ],
        resize_keyboard=True
    )
    return main_menu
