import sys, logging, logging.handlers
import telegram
import keys
from listen import listen

LOG_DIR = 'volume/logs/soyaya.log'

rotating_handler = logging.handlers.RotatingFileHandler(
    LOG_DIR, maxBytes=100000, backupCount=5, encoding='utf-8'
)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO, handlers=[rotating_handler]
)

logging.info('[__main__] program started')
listen()
