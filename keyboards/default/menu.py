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
