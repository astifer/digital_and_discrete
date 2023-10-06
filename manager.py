import random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

import models.keyboards as keyboards
from tools.settings import config
from tools.utils import send_mess, send_mess_kb

from models.user import User 
from models.content import all_tests, all_tests_desription 

import enum
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def drive_test(event: VkLongPoll.DEFAULT_EVENT_CLASS, user: User, vk_api_method, longpoll):
    
    send_mess_kb(event=event, vk_api_method=vk_api_method,
                 keyboard=keyboards.test_choice_keyboard,
                 message='Type exit or...\n'+all_tests_desription)
    
    position='test_choice'
    for event in longpoll.listen():
        
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            if position=='test_choice' and event.text in all_tests:

                user.run_test(test_name=event.text, event=event, longpoll=longpoll, vk_api_method=vk_api_method)
                send_mess_kb(event=event, vk_api_method=vk_api_method,
                            keyboard=keyboards.test_choice_keyboard,
                            message="You have done test! Congrats!")
                
            elif event.text == 'Exit':
                break
            else:
                send_mess_kb(event=event, vk_api_method=vk_api_method,
                            keyboard=keyboards.test_choice_keyboard,
                            message=f"[drive_test]: Comand not found")
                
    
def welcome(event: VkLongPoll.DEFAULT_EVENT_CLASS, vk_api_method, longpoll):
    
    send_mess_kb(event=event, vk_api_method=vk_api_method,
                 keyboard=keyboards.welcome_keyboard,
                 message='You are on welcome page of Test! Lets go? (GO! / exit)')
    
    position='start'
    user = User(event.user_id)
    
    for event in longpoll.listen():
        
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            if event.text.lower() == 'exit':
                break
            
            elif position=='start' and event.text=='GO!':
                vk_api_method.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message='Lets make auth. What is your name?'
                )
                position='wait for name'
                
            elif position=='wait for name' and event.text!='GO!':
                name = event.text
                user.name = name
                send_mess_kb(event=event, vk_api_method=vk_api_method,keyboard=keyboards.menu_keyboard, message=f"Hi, {name}. Here is the main menu:")
                position='menu'
            
            # Menu
            elif position=='menu':
                if event.text == 'Profile':
                    send_mess(event=event, vk_api_method=vk_api_method,
                              message=f'Your profile: {user}')
                    send_mess_kb(event=event, vk_api_method=vk_api_method,keyboard=keyboards.menu_keyboard, message=f"Here is the main menu:")
                    position='menu'
                elif event.text == 'Tests':
                    send_mess(event=event, vk_api_method=vk_api_method,
                              message=f'Lets start doing. We have some tests. Look!')
                    drive_test(event=event, user=user, vk_api_method=vk_api_method, longpoll=longpoll)
                    send_mess_kb(event=event, vk_api_method=vk_api_method,keyboard=keyboards.menu_keyboard, message=f"Here is the main menu:")
                    position = 'menu'
                elif event.text == 'Statistic':
                    send_mess(event=event, vk_api_method=vk_api_method,
                        message=f'Statistic: \n {user.get_statistic()}'
                    )
                    position='menu'
                    send_mess_kb(event=event, vk_api_method=vk_api_method,keyboard=keyboards.menu_keyboard, message=f"Here is the main menu:")
                else:
                    send_mess(event=event, vk_api_method=vk_api_method,
                        message=f'Command not found'
                    )
                    send_mess_kb(event=event, vk_api_method=vk_api_method,keyboard=keyboards.menu_keyboard, message=f"Here is the main menu:")
            
                          
    send_mess(event=event, vk_api_method=vk_api_method, message="Finishing all progress")
    
    
    
