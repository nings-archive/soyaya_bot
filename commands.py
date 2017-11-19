import datetime, logging

THRESHOLD_LAG = datetime.timedelta(seconds=5)

def whodabest(bot, update):
    """Make bot respond 'ning da best' to command"""
    log_body = "{func} call from {user_name}({user_id}) ".format(
        func='whodabest', 
        user_name=update.message.from_user.first_name,
        user_id=update.message.from_user.id
    )
    log_body += ("in private chat" if 
        update.message.chat.title=='' or update.message.chat.title==None
        else "at {group_name}({group_id})".format(
            group_name=update.message.chat.title,
            group_id=update.message.chat.id
        )
    )
    logging.info(log_body)
    # this check prevents spam by backlogged commands 
    timedelta_ago = datetime.datetime.now() - update.message.date
    if timedelta_ago < THRESHOLD_LAG:
        bot.send_message(
            chat_id=update.message.chat_id,
            text='{} da best'.format(update.message.from_user.first_name)
        )
