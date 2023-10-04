import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from settings import GROUP_KEY, KEYBOARD_KEY
from keyboards import keyboard
from utils import get_weather, manage_event

import requests

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


group_key = GROUP_KEY


vk_session = vk_api.VkApi(token=group_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
logging.info('vk_session is created')


for event in longpoll.listen():
    logging.info('Event!'+str(event))
    
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        manage_event(event=event, vk_api_method=vk)
            