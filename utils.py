import requests
from bs4 import BeautifulSoup
import logging
import wikipedia

from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id
from vk_api import VkApiMethod

from keyboards import keyboard
from settings import GROUP_KEY, KEYBOARD_KEY



def get_weather(city: str='москва'):
    city = city.lower()
    request = requests.get('https://sinoptik.ua/погода-'+city)
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


def manage_event(event: VkLongPoll.DEFAULT_EVENT_CLASS, vk_api_method: VkApiMethod):
    message = event.text
    
    if event.text.startswith('+'):
        logging.info('event plus!')
        message = 'oh, plus'
        
    elif event.text.startswith('echo'):
        logging.info('echo event')
        message = event.text.split()[1:]
        
    elif event.text.startswith('wiki'):
        logging.info('wikipedia event')
        subject = ' '.join(event.text.split()[1:])
        try:
            message = wikipedia.summary(subject)
        except LookupError:
            message = 'not found'
            
    elif event.text.startswith('keyboard'):
        logging.info('event keyboard')
        vk_api_method.messages.send(keyboard=keyboard.get_keyboard(),
                            key= (KEYBOARD_KEY),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message='Keyboard:'
                             )
        
    elif event.text.startswith('weather'):
        logging.info('weather event')
        city = ' '.join(event.text.split()[1:])
        message = get_weather(city)
        
    else:
        logging.info('there is the deepest place')
        pass
    
    vk_api_method.messages.send(user_id = event.user_id,
                       random_id = get_random_id(),
                       message = message
                       )
            