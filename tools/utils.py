import requests
import os
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

import vk_api
from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard
from functools import lru_cache

from tools.settings import config

test_count = 3

@lru_cache(maxsize=None)
def send_mess(event, vk_api_method, message):
    vk_api_method.messages.send(
            user_id = event.user_id,
            random_id = get_random_id(),
            message=message
        )
    pass

@lru_cache(maxsize=None)
def send_mess_kb(event, vk_api_method, keyboard: VkKeyboard, message: str):
    vk_api_method.messages.send(keyboard=keyboard.get_keyboard(),
            key= (config.keyboard_key),
            server= ("https://lp.vk.com/whp/222723275"),
            ts = ("121"),
            user_id = event.user_id,
            random_id = get_random_id(),
            message=message
        )
    pass

@lru_cache(maxsize=None)
def check_update(vk_api_method):
    cnt = 0
    logging.info('check new tests')
    
    with open('data/tests.txt', 'r') as f:
        data = f.readlines()
        
        for line in data:
            if line == "$\n":
                cnt+=1
                
        if cnt+1 != test_count and len(data) % 3 ==0:
            add_new_test(vk_api_method)
    pass


def add_new_test(vk_api_method):
    # adding to tests and ...
    
    notify_all_users(vk_api_method)
    

def notify_all_users(vk_api_method):
    
    with open('data/users.txt', 'r') as f:
        users_idx = f.readlines()
        
        for user_id in users_idx:
            vk_api_method.messages.send(
                user_id = int(user_id),
                random_id = get_random_id(),
                message="We add new test!"
            )
            

@lru_cache(maxsize=None)
def send_stat(user, event, vk_api_method, f_name='score_stat'):
    
    upload = vk_api.VkUpload(vk_api_method)
    photo = upload.photo_messages(f'data/{user.id}_{f_name}.jpeg')
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk_api_method.messages.send(user_id=event.user_id, random_id=0, attachment=attachment)
    os.remove(f'data/{user.id}_{f_name}.jpeg')


def get_weather(city: str='москва'):
    try:
        city = city.lower()
        request = requests.get('https://sinoptik.ua/погода-'+'-'.join(city.split()))
        b = BeautifulSoup(request.text, 'html.parser')
        
        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()
        
        result = 'Morning: '+weather1+' '+weather2
        result += ' Day: '+weather3+' '+weather4
    except:
        result = 'not found'
        
    return result

