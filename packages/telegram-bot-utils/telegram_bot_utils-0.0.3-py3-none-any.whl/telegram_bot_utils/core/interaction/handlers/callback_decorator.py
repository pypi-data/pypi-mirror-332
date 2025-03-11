from loguru import logger


def callback_handler(pattern):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Function '{func.__name__}' raised an error: {str(e)}")
                # handle or re-raise the exception appropriately

        wrapper.callback_handler = pattern
        return wrapper

    return decorator
