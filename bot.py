from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    mybot.start_polling()
    mybot.idle()

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Привет {} {}! Ты написал: '{}'".format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: {}, Chat_id: {}, Message: {}".format(update.message.chat.first_name, update.message.chat.id, update.message.text))
    update.message.reply_text(user_text)

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    text = 'Привет {}'.format(emo)
    logging.info(text)
    update.message.reply_text(text)

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/*.jpg')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))

def get_user_emo(user_data):
    if 'emo' in user_data:
        pass
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    return user_data['emo']

main()
