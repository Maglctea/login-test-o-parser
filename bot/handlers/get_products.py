
import requests
from aiogram import types


async def get_products(callback_query: types.CallbackQuery) -> None:
    url = 'http://127.0.0.1:8000/v1/products/'
    response = requests.get(url).json()
    result = 'Вот тебе данные:\n\n'
    for i in range(len(response)):
        result += f'{i+1}) {response[i]["name"]} - {response[i]["url"]}\n\n'

        if len(result) > 3500:
            await callback_query.message.answer(result)
            result = ''
    if result:
        await callback_query.message.answer(result)