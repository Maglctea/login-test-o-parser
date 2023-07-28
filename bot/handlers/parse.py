import requests
from aiogram import types
from aiogram.filters import CommandObject

from bot.bot_texts import ERROR_PARSE, START_PARSE


async def get_poducts_command(message: types.Message) -> None:
    url = 'http://127.0.0.1:8000/v1/products/'
    response = requests.get(url).json()

async def parse_func(message: types.Message) -> None:
    url = 'http://127.0.0.1:8000/v1/products/'
    payload = {'products_count': 10}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        await message.answer(
            START_PARSE,
        )
    else:
        await message.answer(
            ERROR_PARSE,
        )


async def parse_command(message: types.Message, command: CommandObject) -> None:
    return await parse_func(message)
