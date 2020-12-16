from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User

from loader import _
from utils.db_api import db

table_choose_liga = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Бундесліга"), callback_data="m_t_b"),
            InlineKeyboardButton(text=_("АПЛ"), callback_data="m_t_epl"),
        ],
        [
            InlineKeyboardButton(text=_("Ла Ліга"), callback_data="m_t_ll"),
            InlineKeyboardButton(text=_("Ліга 1"), callback_data="m_t_l1"),
        ],
        [
            InlineKeyboardButton(text=_("Серія А"), callback_data="m_t_sa"),
            InlineKeyboardButton(text=_("УПЛ"), callback_data="m_t_upl"),
        ],
    ]
)

scorers_choose_liga = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Бундесліга"), callback_data="m_s_b"),
            InlineKeyboardButton(text=_("АПЛ"), callback_data="m_s_epl"),
        ],
        [
            InlineKeyboardButton(text=_("Ла Ліга"), callback_data="m_s_ll"),
            InlineKeyboardButton(text=_("Ліга 1"), callback_data="m_s_l1"),
        ],
        [
            InlineKeyboardButton(text=_("Серія А"), callback_data="m_s_sa"),
            InlineKeyboardButton(text=_("УПЛ"), callback_data="m_s_upl"),
        ],
    ]
)

assists_choose_liga = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Бундесліга"), callback_data="m_a_b"),
            InlineKeyboardButton(text=_("АПЛ"), callback_data="m_a_epl"),
        ],
        [
            InlineKeyboardButton(text=_("Ла Ліга"), callback_data="m_a_ll"),
            InlineKeyboardButton(text=_("Ліга 1"), callback_data="m_a_l1"),
        ],
        [
            InlineKeyboardButton(text=_("Серія А"), callback_data="m_a_sa"),
            InlineKeyboardButton(text=_("УПЛ"), callback_data="m_a_upl"),
        ],
    ]
)

assists_choose_liga_en = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Бундесліга"), callback_data="m_a_b"),
            InlineKeyboardButton(text=_("АПЛ"), callback_data="m_a_epl"),
        ],
        [
            InlineKeyboardButton(text=_("Ла Ліга"), callback_data="m_a_ll"),
            InlineKeyboardButton(text=_("Ліга 1"), callback_data="m_a_l1"),
        ],
        [
            InlineKeyboardButton(text=_("Серія А"), callback_data="m_a_sa"),
        ],
    ]
)

matches_choose_liga = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Бундесліга"), callback_data="m_m_b"),
            InlineKeyboardButton(text=_("АПЛ"), callback_data="m_m_epl"),
        ],
        [
            InlineKeyboardButton(text=_("Ла Ліга"), callback_data="m_m_ll"),
            InlineKeyboardButton(text=_("Ліга 1"), callback_data="m_m_l1"),
        ],
        [
            InlineKeyboardButton(text=_("Серія А"), callback_data="m_m_sa"),
            InlineKeyboardButton(text=_("УПЛ"), callback_data="m_m_upl"),
        ],
    ]
)
