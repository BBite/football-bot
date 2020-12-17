from aiogram.types import CallbackQuery, User

from loader import dp

from utils.db_api import db


@dp.callback_query_handler(text_contains='m_s_')
async def scorers_handler(call: CallbackQuery):
    await call.message.edit_reply_markup()
    task = call.data.split('_')[-1]
    lang = db.get_lang(User.get_current().id)
    with open(rf'C:\mpr\football-bot\data\scorers\{task}_{lang}.jpg', 'rb') as table_photo:
        await call.message.answer_photo(table_photo)
