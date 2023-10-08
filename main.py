import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from tools.settings import config
from manager import manage_event
from models.content import user_manual
from tools.utils import send_mess, check_update

import requests
import schedule, time, threading


import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def job():
    check_update(vk)

def thr():
    global stop_thr
    while True:
        schedule.run_pending()
        time.sleep(15)
        if stop_thr:
            break
        
stop_thr = False
schedule.every(1).minutes.do(job)
threading.Thread(target=thr).start()

group_key = config.group_key


vk_session = vk_api.VkApi(token=group_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
logging.info('vk_session is created')
is_manual = False



for event in longpoll.listen():
    if not(is_manual):
            vk.messages.send(
                            user_id = event.user_id,
                            random_id = 0,
                            message=user_manual)
            is_manual=True
            
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text.startswith('turn off update'):
            logging.info('turn off update event')
            stop_thr = True
            send_mess(event=event, vk_api_method=vk, message = 'We have turned test update off')
            
        elif event.text.startswith('turn on update'):
            logging.info('turn off update event')
            stop_thr = False
            schedule.every(1).minutes.do(job)
            threading.Thread(target=thr).start()

            send_mess(event=event, vk_api_method=vk, message = 'We have turned test update on')
        else:
            manage_event(event=event, vk_api_method=vk, longpoll=longpoll)

stop_thr = True