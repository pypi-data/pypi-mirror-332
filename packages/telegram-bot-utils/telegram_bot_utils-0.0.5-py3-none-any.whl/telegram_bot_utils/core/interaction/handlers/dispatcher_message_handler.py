from telegram import Update, ForceReply
from telegram.ext import ContextTypes

from validation import ValidationException


async def dispatcher_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message.reply_to_message:
            await handle_reply_message(update, context)
    except ValidationException as e:
        await send_validation_error_message(update, context, str(e))


async def handle_reply_message(update, context):
    reply_text = update.message.reply_to_message.text
    user_data = context.user_data

    for condition, text_snippet, handler in handler_registry:
        if user_data.get(condition) and (text_snippet in reply_text or not text_snippet):
            await invoke_handler(handler, update, context)
            break


async def send_validation_error_message(update, context, error_message):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=error_message,
        reply_markup=ForceReply(selective=True),
    )


async def invoke_handler(handler, update, context):
    if hasattr(handler, '__self__') and handler.__self__ is not None:
        await handler(update, context)  # Bound method
    else:
        await handler(update, context)  # Unbound function or static method


handler_registry = []


def message_handler(condition, text_snippet=""):
    def decorator(func):
        handler_registry.append((condition, text_snippet, func))
        return func

    return decorator
