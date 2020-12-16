from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User

from loader import _
from utils.db_api import db

menu = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Таблиці"), callback_data="menu_t")],
        [
            InlineKeyboardButton(text=_("Топ бомбарадирів"), callback_data="menu_s"),
            InlineKeyboardButton(text=_("Топ асистентів"), callback_data="menu_a"),
        ],
        [
            InlineKeyboardButton(text=_("Розклад матчів"), callback_data="menu_m"),
        ],
    ]
)
