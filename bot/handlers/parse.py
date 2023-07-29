import requests
from aiogram import types
from bot.bot_texts import ERROR_PARSE, START_PARSE
from bot.settings import MAX_ITEMS_PARSED_COUNT, API_LINK


async def parse_func(callback_query: types.CallbackQuery) -> None:  # input number
    payload = {'products_count': MAX_ITEMS_PARSED_COUNT}

    response = requests.post(API_LINK, data=payload)

    if response.status_code == 200:
        await callback_query.answer(
            START_PARSE,
        )
    else:
        await callback_query.answer(
            ERROR_PARSE,
        )
