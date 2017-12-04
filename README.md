# soyaya_bot
A simple telegram bot for USP's Saren house

## Getting Started
You are recommended to run soyaya_bot with [docker](https://www.docker.com/get-docker), in which case docker will be the only dependency. Simply use the built in build and run scripts,

    $ ./build.sh
    $ ./run.sh
    
Alternatively, you may run soyaya_bot directly on your machine. In this case, you will need to have the [`telegram`](https://github.com/python-telegram-bot/python-telegram-bot) module installed.

    # pip3 install python-telegram-bot
    $ python3 soyaya

In both cases, you will have to paste the telegram bot's `api_key` as well as the `chat_id` of `ACCEPTED_GROUPS` in `soyaya/config.py`.
