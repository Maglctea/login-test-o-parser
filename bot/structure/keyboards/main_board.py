from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.structure import MainMenuActions
from bot.structure.callback_data_states import MainMenuCallback

builder = InlineKeyboardBuilder()

builder.button(
    text="Начать парсинг", callback_data=MainMenuCallback(action=MainMenuActions.START_PARSING)
)
builder.button(
    text="Покажи данные", callback_data=MainMenuCallback(action=MainMenuActions.SHOW_DATA)
)
builder.adjust(1)

MAIN_BOARD = builder.as_markup()
