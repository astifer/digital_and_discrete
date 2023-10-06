import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard
from functools import lru_cache

from tools.settings import config

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

def get_weather(city: str='москва'):
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
    
    return result

