import logging, os
from glob import glob
from random import choice

from emoji import emojize

from utils import get_user_emo, get_keyboard, is_cat
import settings

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Привет {} {}! Ты написал: '{}'".format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: {}, Chat_id: {}, Message: {}".format(update.message.chat.first_name, update.message.chat.id, update.message.text))
    update.message.reply_text(user_text, reply_markup=get_keyboard())

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    text = 'Привет {}'.format(emo)
    logging.info(text)
    update.message.reply_text(text, reply_markup=get_keyboard())

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/*.jpg')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())

def change_avatar(bot, update, user_data):
    user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    text = 'Аватар изменен: {}'.format(user_data['emo'])
    update.message.reply_text(text, reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
    contact = update.message.contact
    text = 'Спасибо {}, твой номер: {}'.format(get_user_emo(user_data), contact['phone_number'])
    update.message.reply_text(text, reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    location = update.message.location
    text = 'Спасибо {}, твои координаты: {}'.format(get_user_emo(user_data), str(location))
    update.message.reply_text(text, reply_markup=get_keyboard())

def check_user_photo(bot, update, user_data):
    update.message.reply_text("Обрабатываю фото")
    os.makedirs('downloads', exist_ok=True)
    photo_file = bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', '{}.jpg'.format(photo_file.file_id))
    photo_file.download(filename)
    if is_cat(filename):
        update.message.reply_text("Найден котэ, добавляю в библиотеку")
        new_filename = os.path.join('images', 'cat_{}.jpg'.format(photo_file.file_id))
        os.rename(filename, new_filename)
    else:
        update.message.reply_text("Котик не обнаружен!")
        os.remove(filename)