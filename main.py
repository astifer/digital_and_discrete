import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from settings import config
from utils import manage_event

import requests

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
qq

group_key = config.group_key


vk_session = vk_api.VkApi(token=group_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
logging.info('vk_session is created')


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        manage_event(event=event, vk_api_method=vk, longpoll=longpoll)
            