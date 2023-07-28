"""
Main
"""
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.bot_texts import BOT_COMMANDS_INFO
from bot.handlers import *
from bot.middleware.permission_check import PermissionCheckMiddleware
from bot.settings import BOT_KEY, logger

from aiogram.fsm.storage.redis import RedisStorage

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

from bot.utils.consumer import check_redis_message


async def async_main() -> None:
    # init bot
    storage = RedisStorage.from_url("redis://localhost:16379/0")
    bot = Bot(token=BOT_KEY)
    dp = Dispatcher(storage=storage)

    # help commands
    commands_for_bot = []
    for cmd in BOT_COMMANDS_INFO:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(commands_for_bot)

    # add handlers

    register_user_commands(dp)

    logging.getLogger('apscheduler').setLevel(logging.WARNING)
    # add message consumer
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        check_redis_message,
        trigger="interval",
        seconds=1,
        kwargs={
            "redis": storage,
            "bot": bot,
        }
    )
    scheduler.start()

    dp.message.middleware.register(PermissionCheckMiddleware())
    await dp.start_polling(bot)


def main():
    try:
        asyncio.run(async_main())
    except (KeyboardInterrupt, SystemExit):
        logger.debug("Bot stopped")


if __name__ == "__main__":
    main()
