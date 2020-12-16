from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, User

from loader import _
from utils.db_api import db

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_('Меню', lang=db.get_lang(User.get_current().id))),
            # KeyboardButton(text='Ігра')
        ],
        [
            KeyboardButton(text=_('Змінити мову', lang=db.get_lang(User.get_current().id)))
        ]
    ],
    resize_keyboard=True
)
