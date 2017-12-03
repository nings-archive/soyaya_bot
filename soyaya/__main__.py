import sys, logging, logging.handlers
from logging.handlers import RotatingFileHandler
import telegram
from listen import listen

# Set-up logging
LOG_DIR = 'volume/logs/soyaya.log'
rotating_handler = RotatingFileHandler(
    LOG_DIR, maxBytes=100000, backupCount=5, encoding='utf-8'
)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO, handlers=[rotating_handler]
)

# Start soyaya_bot
logging.info('[__main__] program started')
listen()
