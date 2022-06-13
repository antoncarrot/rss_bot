from typing import List, Tuple

from aiogram.types import BotCommand

__all__ = ["HandlersRepository"]


class HandlersRepository:
    _msg_handlers: List[Tuple] = []
    _callback_handlers: List[Tuple] = []
    _commands: List[BotCommand] = []

    @classmethod
    def message_handler(
        cls,
        callback=None,
        *,
        filters=None,
        commands: List[str] = None,
        regexp=None,
        content_types=None,
        state=None,
        run_task=None,
        description=None,
        **kwargs,
    ):
        def decorator(callback):
            _args = [callback]
            if filters:
                _args += filters
            _kwargs = {
                "commands": commands,
                "regexp": regexp,
                "content_types": content_types,
                "state": state,
                "run_task": run_task,
            }
            _kwargs.update(kwargs)
            cls._msg_handlers.append((_args, _kwargs))
            if description:
                for cmd in commands:
                    cls._commands.append(BotCommand(command=cmd, description=description))
            return callback

        if callback is None:
            return decorator
        return decorator(callback)

    @classmethod
    def callback_handler(
        cls,
        callback=None,
        *,
        filters=None,
        state=None,
        run_task=None,
        **kwargs,
    ):
        def decorator(callback):
            _args = [callback]
            if filters:
                _args += filters
            _kwargs = {
                "state": state,
                "run_task": run_task,
            }
            _kwargs.update(kwargs)
            cls._callback_handlers.append((_args, _kwargs))
            return callback

        if callback is None:
            return decorator
        return decorator(callback)

    @classmethod
    async def register_handlers(cls, dp):
        for _args, _kwargs in cls._msg_handlers:
            dp.register_message_handler(*_args, **_kwargs)
        for _args, _kwargs in cls._callback_handlers:
            dp.register_callback_query_handler(*_args, **_kwargs)
        await dp.bot.set_my_commands(cls._commands)
