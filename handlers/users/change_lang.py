from aiogram.types import Message, CallbackQuery, User

from loader import dp, _

from keyboards.inline import choose_language

from utils.db_api import db


@dp.message_handler(text=_('Змінити мову'))
async def bot_start(message: Message):
    await message.answer(_('Виберіть мову'), reply_markup=choose_language)


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    db.update('users', User.get_current().id, {
        'lang': lang
    })
    await call.message.edit_text(_("Мова була змінена", locale=lang))
