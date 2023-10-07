import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from tools.settings import config
from manager import manage_event
from models.content import user_manual

import requests

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


group_key = config.group_key


vk_session = vk_api.VkApi(token=group_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
logging.info('vk_session is created')
is_manual = False

# for event in longpoll.listen():
#     if not(is_manual):
#             vk.messages.send(
#                             user_id = event.user_id,
#                             random_id = 0,
#                             message=user_manual)
#             is_manual=True
            
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         manage_event(event=event, vk_api_method=vk, longpoll=longpoll)
            