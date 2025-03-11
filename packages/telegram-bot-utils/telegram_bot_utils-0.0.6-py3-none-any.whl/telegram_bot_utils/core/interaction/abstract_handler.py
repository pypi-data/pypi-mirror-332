import asyncio

from telegram.ext import CallbackQueryHandler


class ButtonHandler(CallbackQueryHandler):
    def __init__(self, handler, pattern):
        super().__init__(handler, pattern=pattern)

    async def handle_update(self, *args):
        asyncio.create_task(super().handle_update(*args))
