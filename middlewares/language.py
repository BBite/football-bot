from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from data.config import I18N_DOMAIN, LOCALES_DIR

from typing import Tuple, Any

from utils.db_api import db


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()
        # print(db.get_lang(user.id))
        # print(db.get_lang(user.id) or user.locale)
        return db.get_lang(user.id) or user.locale


def setup_lang_middleware(dp):
    i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
