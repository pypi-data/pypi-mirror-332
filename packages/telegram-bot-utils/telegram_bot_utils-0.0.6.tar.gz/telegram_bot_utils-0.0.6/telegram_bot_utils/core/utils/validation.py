from functools import wraps

def validate_message(validator_class):
    def decorator(handler_func):
        @wraps(handler_func)
        def wrapper(update, context):
            # Validate the Solana address
            if validator_class.validate(update.message.text):
                return handler_func(update, context)
            else:
                raise ValidationException(validator_class.error_msg())

        return wrapper

    return decorator


class MessageValidator:
    @staticmethod
    def validate(message):
        pass

    @staticmethod
    def error_msg():
        return "Message data invalid"


class ValidationException(Exception):
    pass
