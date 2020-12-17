from aiogram.types import CallbackQuery, User, Message

from loader import dp

from utils.db_api import db


@dp.callback_query_handler(text_contains='m_a_')
async def assists_handler(call: CallbackQuery):
    await call.message.edit_reply_markup()
    task = call.data.split('_')[-1]
    lang = db.get_lang(User.get_current().id)
    if task == 'upl' and lang == 'en':
        await call.message.answer('Assistants for this league has not been given')
    else:
        with open(rf'C:\mpr\football-bot\data\assists\{task}_{lang}.jpg', 'rb') as table_photo:
            await call.message.answer_photo(table_photo)
