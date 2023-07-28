"""
command help
"""
from aiogram import types
from aiogram.filters import CommandObject

from bot.bot_texts import TEXT_HELP, BOT_COMMANDS_INFO


async def help_func(message: types.Message):
    """
    help main
    :param message:
    :return:
    """
    return await message.answer(
        TEXT_HELP
    )


async def help_command(message: types.Message, command: CommandObject):
    """
    help command detail
    :param message:
    :param command:
    :return:
    """
    if command.args:
        for cmd in BOT_COMMANDS_INFO:
            if cmd[0] == command.args:
                return await message.answer(
                    f"{cmd[0]} - {cmd[1]}\n\n{cmd[2]}"
                )
        else:
            return await message.answer("Команда не найдена")
    return await help_func(message)
