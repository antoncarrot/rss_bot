import asyncio
import logging

from .tg_bot import init_tg_bot

logger = logging.getLogger(__name__)


async def main():
    dp = await init_tg_bot()
    logger.info("Starting bot")
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await dp.bot.get_session().close()


asyncio.run(main())
