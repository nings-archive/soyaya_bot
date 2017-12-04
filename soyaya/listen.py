import logging
import telegram, telegram.ext
import user, config, utils
from config import API_KEY

ABOUT_MESSAGE = '''
`soyaya_bot` is a telegram bot for USP's Saren house.
Submit PRs/issues at [github](https://github.com/ningyuansg/soyaya_bot), \
or contact @ningyuan
'''

updater = telegram.ext.Updater(token=config.API_KEY)
set_me_is_active = utils.Set_me_is_active()
handlers = []

@utils.restrict_to_allowed_groups
def register(bot, update):
    user_id, chat_id, first_name = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    this_user = user.User(user_id)
    log_body = '[listen] [register] call by {} ({}) at {}'.format(
        user_id, first_name, chat_id
    )
    if this_user.is_registered():
        bot.send_message(chat_id=chat_id, text='You are already registered!')
        log_body += ', but user is already registered.'
    else:
        this_user.make_new_user_data()
        this_user.save_data()
        bot.send_message(
            chat_id=chat_id, 
            text='Registration completed for {}!'.format(first_name)
        )
        log_body += ', and registration successful'
    logging.info(log_body)

@utils.restrict_to_registered
def me(bot, update):
    user_id, chat_id, first_name = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    this_user = user.User(user_id)
    log_body = '[listen] [me] call by {} ({}) at {}'.format(
        user_id, first_name, chat_id
    )
    this_user.load_data()
    bot.send_message(
        chat_id=chat_id,
        text='{} {}'.format(first_name, this_user.data['me_message'])
    )
    logging.info(log_body)

@utils.restrict_to_registered
@utils.restrict_to_pms
def set_me(bot, update):
    user_id, chat_id, first_name = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    log_body = '[listen] [set_me] call by {} ({}) at {}'.format(
        user_id, first_name, chat_id
    )
    this_user = user.User(user_id)
    if not this_user.is_registered():
        bot.send_message(chat_id=chat_id, 
            text='Please /register first!'
        )
        log_body += ', but user is not registered'
    else:
        set_me_is_active.add_user(user_id)
        bot.send_message(chat_id=chat_id,
            text='Enter your new /me message (max 80 chars)'
        )
        log_body += ', and user added to set_me_is_active'
    logging.info(log_body)

def set_me_message(bot, update):
    user_id, chat_id, first_name = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    log_body = '[listen] [set_me_message] call by {} ({}) at {}'.format(
        user_id, first_name, chat_id
    )
    new_me_message = update.message.text
    if len(new_me_message) > 80:
        bot.send_message(chat_id=chat_id,
            text='Please limit your /me message to 80 chars!'
        )
        log_body += ', but message exceeds 80 char'
    else:
        this_user = user.User(user_id)
        this_user.load_data()
        this_user.set_me_message(new_me_message)
        this_user.save_data()
        bot.send_message(chat_id=chat_id,
            text='Success!'
        )
        log_body += ', and set_me successful'
        set_me_is_active.del_user(user_id)
    logging.info(log_body)

def cancel(bot, update):
    user_id, chat_id, first_name = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    log_body = '[listen] [cancel] call by {} ({})'.format(
        user_id, first_name, chat_id
    )
    set_me_is_active.del_user(user_id)
    logging.info(log_body)

def about(bot, update):
    user_id, chat_id, first_name = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    log_body = '[listen] [about] call by {} ({})'.format(
        user_id, first_name, chat_id
    )
    bot.send_message(chat_id=chat_id,
        text=ABOUT_MESSAGE, parse_mode=telegram.ParseMode.MARKDOWN
    )
    logging.info(log_body)
    

handlers.append(telegram.ext.CommandHandler('register', register))
handlers.append(telegram.ext.CommandHandler('me', me))
handlers.append(telegram.ext.CommandHandler('set_me', set_me))
handlers.append(telegram.ext.MessageHandler(
    set_me_is_active & telegram.ext.Filters.text, set_me_message
))
handlers.append(telegram.ext.CommandHandler('cancel', cancel))
handlers.append(telegram.ext.CommandHandler('about', about))
for handler in handlers:
    updater.dispatcher.add_handler(handler)

def listen():
    updater.start_polling()
    logging.info('[listen] start_polling call')
    updater.idle()
