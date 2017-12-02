import logging
import telegram, telegram.ext
import user, keys

updater = telegram.ext.Updater(token=keys.api_key)
handlers = []

def register(bot, update):
    userid, chatid, firstname = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    this_user = user.User(userid)
    log_body = '[listen] [register] call by {}'.format(
        this_user.user_id
    )
    if this_user.is_registered():
        bot.send_message(chat_id=chatid, text='You are already registered!')
        log_body += ', but user is already registered.'
    else:
        this_user.make_new_user_data()
        this_user.save_data()
        bot.send_message(
            chat_id=chatid, 
            text='Registration completed for {}!'.format(firstname)
        )
        log_body += ', and registration successful.'
    logging.info(log_body)

def me(bot, update):
    userid, chatid, firstname = (
        update.message.from_user.id,
        update.message.chat_id,
        update.message.from_user.first_name
    )
    this_user = user.User(userid)
    log_body = '[listen] [me] call by {}'.format(
        this_user.user_id
    )
    if not this_user.is_registered():
        bot.send_message(chat_id=chatid, 
            text='Please /register first!')
        log_body += ', but user is not registered'
    else:
        this_user.load_data()
        bot.send_message(
            chat_id=chatid,
            text='{} {}'.format(firstname, this_user.data['me_message'])
        )
        log_body += ', and me_message sent'
    logging.info(log_body)

handlers.append(telegram.ext.CommandHandler('register', register))
handlers.append(telegram.ext.CommandHandler('me', me))
for handler in handlers:
    updater.dispatcher.add_handler(handler)

def listen():
    updater.start_polling()
    logging.info('[listen] start_polling call')
