import requests
from aiogram import types
from bot.settings import API_LINK


async def send_products_list(response, callback_query: types.CallbackQuery) -> None:
    result = 'Вот тебе данные:\n\n'
    for i in range(len(response)):
        result += f'{i + 1}) {response[i]["name"]} - {response[i]["url"]}\n\n'

        if len(result) > 3500:
            await callback_query.message.answer(result)
            result = ''
    if result:
        await callback_query.message.answer(result)


async def get_products(callback_query: types.CallbackQuery) -> None:
    url = API_LINK
    response = requests.get(url).json()
    await send_products_list(response, callback_query)
