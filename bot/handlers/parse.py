import requests
from aiogram import types

from bot.bot_texts import ERROR_PARSE, START_PARSE


async def parse_func(callback_query: types.CallbackQuery) -> None:  # input number
    url = 'http://127.0.0.1:8000/v1/products/'
    payload = {'products_count': 50}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        await callback_query.answer(
            START_PARSE,
        )
    else:
        await callback_query.answer(
            ERROR_PARSE,
        )
