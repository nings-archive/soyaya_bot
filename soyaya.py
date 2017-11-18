#! /usr/bin/env python3
import logging, logging.handlers
from telegram.ext import Updater, CommandHandler
import commands
from keys import api_key

rotating_handler = logging.handlers.RotatingFileHandler(
    'volume/soyaya.log', maxBytes=10000, backupCount=5, encoding='utf-8'
)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO, handlers=[rotating_handler]
)
logging.info('Program start')

whodabest_handler = CommandHandler('whodabest', commands.whodabest)

updater = Updater(token=api_key)
updater.dispatcher.add_handler(whodabest_handler)
updater.start_polling()
