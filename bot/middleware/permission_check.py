from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from bot.bot_texts import PERMISSION_DENIED_MESSAGE
from bot.settings import ADMINS_IDS, ADMINS_USERNAMES


class PermissionCheckMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id in ADMINS_IDS or event.from_user.username in ADMINS_USERNAMES:
            return await handler(event, data)

        return await event.answer(PERMISSION_DENIED_MESSAGE)
