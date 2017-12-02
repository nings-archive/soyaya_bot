import sys, logging, logging.handlers
import telegram
import keys
from cli import *
from look import look
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

cli = Cli(sys.argv[1:])
if cli.args.command == 'listen':
    listen()
elif cli.args.command == 'look':
    look()
