"""
start handler
"""
from aiogram import types
import requests
from bot.bot_texts import GREETING_TEXT


async def start(message: types.Message) -> None:
    await message.answer(
        GREETING_TEXT,
    )
