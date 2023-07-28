__all__ = [
    "register_user_commands",
]

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.handlers.get_products import get_products
from bot.handlers.help import help_command, help_func
from bot.handlers.parse import parse_func
from bot.handlers.start import start
from bot.structure import MainMenuCallback, MainMenuActions


def register_user_commands(router: Router) -> None:
    """
    Register user commands
    :param router:
    :return:
    """
    # start
    router.message.register(start, CommandStart())

    # help
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_func, F.text.capitalize() == "Помощь")

    # parse
    router.message.register(parse_func, F.text.capitalize() == "Начать парсинг")
    router.callback_query.register(parse_func, MainMenuCallback.filter(
        F.action == MainMenuActions.START_PARSING
    ))

    router.message.register(get_products, F.text.capitalize() == "Покажи данные")
    router.callback_query.register(get_products, MainMenuCallback.filter(
        F.action == MainMenuActions.SHOW_DATA
    ))
