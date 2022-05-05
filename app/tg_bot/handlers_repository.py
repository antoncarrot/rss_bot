from typing import Dict, List

from aiogram.types import BotCommand

__all__ = ["HandlersRepository"]


class HandlersRepository:
    _msg_handlers: List[Dict] = []
    _commands: List[BotCommand] = []

    @classmethod
    def message_handler(
        cls,
        callback=None,
        *,
        commands: List[str] = None,
        regexp=None,
        content_types=None,
        state=None,
        run_task=None,
        description=None,
        **kwargs,
    ):
        def decorator(callback):
            conf = {
                "callback": callback,
                "commands": commands,
                "regexp": regexp,
                "content_types": content_types,
                "state": state,
                "run_task": run_task,
            }
            cls._msg_handlers.append(conf)
            if description:
                for cmd in commands:
                    cls._commands.append(BotCommand(command=cmd, description=description))
            return callback

        if callback is None:
            return decorator
        return decorator(callback)

    @classmethod
    async def register_handlers(cls, dp):
        for handler_conf in cls._msg_handlers:
            dp.register_message_handler(**handler_conf)
        await dp.bot.set_my_commands(cls._commands)
