import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from settings import GROUP_KEY, KEYBOARD_KEY
from keyboards import keyboard
from utils import get_weather

import requests
import wikipedia
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)




group_key = GROUP_KEY


vk_session = vk_api.VkApi(token=group_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
print('vk_session is created')


for event in longpoll.listen():
    print('Event!'+str(event))
    
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        
        ev_text = event.text
        if (ev_text.startswith('+')):
            print('event plus!')
            vk.messages.send(user_id = event.user_id,
                             random_id = get_random_id(),
                             message = 'oh, plus'
                             )
        elif (ev_text.startswith('погода') or ev_text.startswith('weather')):
            print("event weather")
            try:
                weather = get_weather(ev_text.split()[1])
            except:
                weather = 'not found'
                
            vk.messages.send(user_id = event.user_id,
                             random_id = get_random_id(),
                             message = weather
                             )
        elif (ev_text.startswith('wiki') or ev_text.startswith('вики')):
            print('wikipedia event')
            subject = str(ev_text.split()[1])

            try:
                result = wikipedia.summary(subject)
            except:
                result = 'not found'
                
            vk.messages.send(user_id = event.user_id,
                             random_id = get_random_id(),
                             message = result
                             )
        elif (ev_text.startswith('keyboard')):
            print('event keyboard')
            vk.messages.send(keyboard=keyboard.get_keyboard(),
                             key= (KEYBOARD_KEY),
                            server= ("https://lp.vk.com/whp/222723275"),
                             ts = ("121"),
                             user_id = event.user_id,
                             random_id = get_random_id(),
                             message='Keyboard:'
                             )
        else:
            print('echo event')
            vk.messages.send(user_id = event.user_id,
                       random_id = get_random_id(),
                       message = ev_text
                       )