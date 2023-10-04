import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


from bs4 import BeautifulSoup

import requests
import wikipedia


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
    

group_key = ""


vk_session = vk_api.VkApi(token=group_key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
print('vk_session is created')




keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Hello', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Goodbay', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=222723275")
print('keyboard is created')



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
                             key= (),
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