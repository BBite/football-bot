from aiogram.types import Message, CallbackQuery, User, ReplyKeyboardRemove

from loader import dp, _

from keyboards.inline import choose_language
from keyboards.default.menu import get_main_menu

from utils.db_api import db


@dp.message_handler(text=[_('Змінити мову'), '/lang'])
async def bot_start(message: Message):
    await message.answer(_('Виберіть мову'), reply_markup=choose_language)


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    db.update('users', User.get_current().id, {
        'lang': lang
    })
    # await call.message.edit_text(_("Мова була змінена", locale=lang))
    full_lang = {
        'uk': 'українська',
        'ru': 'русский',
        'en': 'English'
    }
    await call.message.answer(_("Мова була змінена", locale=lang), reply_markup=ReplyKeyboardRemove())
    await call.message.answer(_('Ваша поточна мова', locale=lang) + f': {full_lang[lang]}',
                              reply_markup=get_main_menu(db.get_lang(User.get_current().id)))
