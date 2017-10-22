#! /usr/bin/env python3
import datetime, logging
from telegram.ext import Updater, CommandHandler
import keys # use keys.api_key

THRESHOLD_LAG = datetime.timedelta(seconds=5)

def whodabest(bot, update):
    timedelta_ago = datetime.datetime.now() - update.message.date
    if timedelta_ago < THRESHOLD_LAG:
        bot.send_message(
            chat_id=update.message.chat_id,
            text='ning da best'
        )

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('').info('logging loaded')

whodabest_handler = CommandHandler('whodabest', whodabest)

updater = Updater(token=keys.api_key)
updater.dispatcher.add_handler(whodabest_handler)
updater.start_polling()
