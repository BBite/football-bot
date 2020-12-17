from aiogram.types import Message, CallbackQuery, User

from loader import dp, _

from keyboards.inline import menu, table_choose_liga, scorers_choose_liga, assists_choose_liga, matches_choose_liga
from keyboards.inline import assists_choose_liga_en

from utils.db_api import db


@dp.message_handler(text=[_('Меню'), '/menu'])
async def bot_start(message: Message):
    await message.answer(_('Меню'), reply_markup=menu)


@dp.callback_query_handler(text_contains='menu_')
async def change_language(call: CallbackQuery):
    await call.message.edit_text(_('Виберіть лігу'))
    task = call.data[-1]
    if task == 't':
        await call.message.edit_reply_markup(table_choose_liga)
    elif task == 's':
        await call.message.edit_reply_markup(scorers_choose_liga)
    elif task == 'a':
        if db.get_lang(User.get_current().id) != 'en':
            await call.message.edit_reply_markup(assists_choose_liga)
        else:
            await call.message.edit_reply_markup(assists_choose_liga_en)
    elif task == 'm':
        await call.message.edit_reply_markup(matches_choose_liga)


@dp.message_handler(commands=['table', 'scorers', 'assists', 'matches'])
async def command_handler(message: Message):
    task = message.text[1]
    if task == 't':
        await message.answer(_('Виберіть лігу'), reply_markup=table_choose_liga)
    elif task == 's':
        await message.answer(_('Виберіть лігу'), reply_markup=scorers_choose_liga)
    elif task == 'a':
        if db.get_lang(User.get_current().id) != 'en':
            await message.answer(_('Виберіть лігу'), reply_markup=assists_choose_liga)
        else:
            await message.answer(_('Виберіть лігу'), reply_markup=assists_choose_liga_en)
    elif task == 'm':
        await message.answer(_('Виберіть лігу'), reply_markup=matches_choose_liga)
