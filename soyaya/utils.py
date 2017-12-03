import logging
from telegram.ext import BaseFilter
from functools import wraps
from config import ACCEPTED_GROUPS

class Set_me_is_active(BaseFilter):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def del_user(self, user):
        # the functional approach deletes all instances
        self.users = list(filter(lambda u: u != user, self.users))
        
    def filter(self, message):
        return message.from_user.id in self.users

def restrict_to_pms(func):
    @wraps(func)
    def wrapped(bot, update):
        if update.message.from_user.id == update.message.chat_id:
            return func(bot, update)
        else:
            bot.send_message(chat_id=update.message.chat_id,
                text='Please private message the bot for /set_me!'
            )
    return wrapped

def restrict_to_allowed_groups(func):
    @wraps(func)
    def wrapped(bot, update):
        if update.message.chat_id in ACCEPTED_GROUPS.values():
            return func(bot, update)
        else:
            bot.send_message(chat_id=update.message.chat_id,
                text='Please /register in the Asgard group chat!'
            )
    return wrapped


