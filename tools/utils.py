import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

import wikipedia

from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard
from functools import lru_cache

from models.keyboards import *
from tools.settings import config
from manager import welcome

@lru_cache(maxsize=None)
def send_mess(event, vk_api_method, message):
    vk_api_method.messages.send(
            user_id = event.user_id,
            random_id = get_random_id(),
            message=message
        )
    pass

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


def manage_event(event: VkLongPoll.DEFAULT_EVENT_CLASS, vk_api_method, longpoll):
    message = event.text
    if event.text.startswith('help'):
        logging.info('help event')
        message = 'What i can do: \n wikipedia: ... \n weather: ... \n tests:...'
        
    elif event.text.startswith('tests'):
        logging.info('tests event')
        welcome(event=event, vk_api_method=vk_api_method, longpoll=longpoll)
        return
        
    elif event.text.startswith('+'):
        logging.info('event plus!')
        message = 'oh, plus'
        
    elif event.text.startswith('echo'):
        logging.info('echo event')
        message = event.text.split()[1:]
        
    elif event.text.startswith('wikipedia'):
        logging.info('wikipedia event')
        subject = ' '.join(event.text.split()[1:])
        try:
            message = wikipedia.summary(subject)
        except LookupError(f"wikipedia couldnt find information about subject: {subject}"):
            message = 'subject not found'
            
    elif event.text.startswith('keyboard'):
        logging.info('event keyboard')
        vk_api_method.messages.send(keyboard=test_keyboard.get_keyboard(),
            key= (config.keyboard_key),
            server= ("https://lp.vk.com/whp/222723275"),
            ts = ("121"),
            user_id = event.user_id,
            random_id = get_random_id(),
            message='Keyboard:'
        )
        return
        
    elif event.text.startswith('weather'):
        logging.info('weather event')
        city = ' '.join(event.text.split()[1:])
        message = get_weather(city)
        
    else:
        pass
    
    vk_api_method.messages.send(user_id = event.user_id,
                       random_id = get_random_id(),
                       message = message
                       )
            
