from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User

from loader import _
from utils.db_api import db

menu = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Таблиці", lang=db.get_lang(User.get_current().id)), callback_data="menu_t")],
        [
            InlineKeyboardButton(text=_("Топ бомбарадирів", lang=db.get_lang(User.get_current().id)),
                                 callback_data="menu_s"),
            InlineKeyboardButton(text=_("Топ асистентів", lang=db.get_lang(User.get_current().id)),
                                 callback_data="menu_a"),
        ],
        [
            InlineKeyboardButton(text=_("Розклад матчів", lang=db.get_lang(User.get_current().id)),
                                 callback_data="menu_m"),
        ],
    ]
)
