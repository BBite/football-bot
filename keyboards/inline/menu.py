from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Таблиці", callback_data="menu_t")],
        [
            InlineKeyboardButton(text="Топ бомабрадирів", callback_data="menu_s"),
            InlineKeyboardButton(text="Топ асистентів", callback_data="menu_a"),
        ],
        [
            InlineKeyboardButton(text="Розклад матчів", callback_data="menu_m"),
        ],
    ]
)
