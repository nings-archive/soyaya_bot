import user
from config import ACCEPTED_GROUPS

def restrict_to(pred, err_msg):
    '''e.g. @restrict_to(is_private_message, 'PLS PM')'''
    def decorator(func):
        def modified_func(bot, update):
            if pred(update):
                return func(bot, update)
            else:
                bot.send_message(chat_id=update.message.chat_id,
                    text=err_msg
                )
        return modified_func
    return decorator

def is_private_message(update):
    return update.message.from_user.id == update.message.chat_id

def is_allowed_group(update):
    return update.message.chat_id in ACCEPTED_GROUPS.values()

def is_registered(update):
    return user.User(update.message.from_user.id).is_registered()
