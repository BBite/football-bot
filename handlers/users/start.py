from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, User

from loader import dp

from utils.db_api import db

from keyboards.inline import choose_language
from keyboards.default import main_menu


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer('Привіт, Бидло!', reply_markup=main_menu)
    db.insert('users', {
        'id': User.get_current().id,
        'first_name': User.get_current().first_name,
        'last_name': User.get_current().last_name,
        'lang': User.get_current().locale.language
    })
    await message.answer('Виберіть мову', reply_markup=choose_language)
