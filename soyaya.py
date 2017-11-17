#! /usr/bin/env python3
import datetime, logging
from telegram.ext import Updater, CommandHandler
import commands
from keys import api_key

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logging.info('Program start')

whodabest_handler = CommandHandler('whodabest', commands.whodabest)

updater = Updater(token=api_key)
updater.dispatcher.add_handler(whodabest_handler)
updater.start_polling()
