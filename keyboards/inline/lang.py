from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose_language = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Українська", callback_data="lang_uk")],
        [
            InlineKeyboardButton(text="Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="English", callback_data="lang_en"),
        ]
    ]
)
