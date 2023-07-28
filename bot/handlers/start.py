"""
start handler
"""
from aiogram import types
import requests
from bot.bot_texts import GREETING_TEXT
from bot.structure.keyboards import MAIN_BOARD


async def start(message: types.Message) -> None:
    await message.answer(
        GREETING_TEXT,
        reply_markup=MAIN_BOARD
    )
