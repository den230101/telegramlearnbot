from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from clarifai.rest import ClarifaiApp

import settings

def get_user_emo(user_data):
    if 'emo' in user_data:
        pass
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    return user_data['emo']


def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact=True)
    location_button = KeyboardButton('Прислать координаты', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
        ['Прислать котика', 'Сменить аватар'],
        [contact_button, location_button]
        ], resize_keyboard=True)
    return my_keyboard

def is_cat(file_name):
    image_has_cat = False
    app = ClarifaiApp(api_key=settings.CLARIFY_API_KEY)
    model = app.public_models.general_model
    response = model.predict_by_filename(file_name, max_concepts=5)
    #import pprint
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(response)
    for concept in response['outputs'][0]['data']['concepts']:
        if concept['name'] == 'cat':
            image_has_cat = True
    return image_has_cat

if __name__ == '__main__':
    print(is_cat('images/2567542298.jpg'))