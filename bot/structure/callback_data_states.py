import enum

from aiogram.filters.callback_data import CallbackData


class MainMenuActions(enum.IntEnum):
    """
        Statistic actions
    """
    START_PARSING = 0
    SHOW_DATA = 2


class MainMenuCallback(CallbackData, prefix="statistic"):
    """
    Statistic callback
    """
    action: MainMenuActions
