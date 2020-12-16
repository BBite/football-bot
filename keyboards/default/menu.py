from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            # KeyboardButton(text='Ігра')
        ],
        [
            KeyboardButton(text='Змінити мову')
        ]
    ],
    resize_keyboard=True
)
