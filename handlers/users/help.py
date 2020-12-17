from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, _
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        _('Список команд') + ': ',
        '/start - ' + _('Запустити бота'),
        '/help - ' + _('Отримати список команд'),
        '/lang - ' + _('Змінити мову'),
        '/menu - ' + _('Відкрити меню'),
        '/table - ' + _('Відкрити таблицю результатів'),
        '/scorers - ' + _('Відкрити топ бомбрадирів'),
        '/assists - ' + _('Відкрити топ асистентів'),
        '/matches - ' + _('Відкдити розклад матчів')
    ]
    await message.answer('\n'.join(text))
