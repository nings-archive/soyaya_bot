import sys
import telegram
import keys
from cli import *
from look import look
from listen import listen

cli = Cli(sys.argv[1:])
bot = telegram.Bot(token=keys.api_key)

if cli.args.command == 'listen':
    listen()
elif cli.args.command == 'look':
    look()
