from aiogram.fsm.storage.redis import RedisStorage
from bot.settings import ADMINS_IDS


async def handle_message(bot, message: bytes):
    for admin in ADMINS_IDS:
        await bot.send_message(admin, f"Сохранено: {message.decode().split()[2]} товаров")


async def check_redis_message(redis: RedisStorage, bot):
    message = await redis.redis.lpop('parser')

    if message:
        print(message)
        await handle_message(bot, message)
