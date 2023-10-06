import random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

import models.keyboards as keyboards
from tools.settings import config
from models.user import User 
from models.content import all_tests, all_tests_desription 

import enum
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def drive_test(event: VkLongPoll.DEFAULT_EVENT_CLASS, user: User, vk_api_method, longpoll):
    vk_api_method.messages.send(
                            keyboard=keyboards.test_choice_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message='Type exit or...\n'+all_tests_desription
                            )
    
    position='test_choice'
    for event in longpoll.listen():
        
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            if position=='test_choice' and event.text in all_tests:

                user.run_test(test_name=event.text, event=event, longpoll=longpoll, vk_api_method=vk_api_method)
                vk_api_method.messages.send(
                            keyboard=keyboards.test_choice_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message="You have done test! Congrats!"
                            )
            elif event.text == 'Exit':
                break
            else:
                vk_api_method.messages.send(
                            keyboard=keyboards.test_choice_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message=f"[drive_test]: Comand not found"
                            )
                
                
def send_menu(event, vk_api_method, message='Here is the main menu'):
    vk_api_method.messages.send(
                    keyboard=keyboards.menu_keyboard.get_keyboard(),
                    key= (config.keyboard_key),
                    server= ("https://lp.vk.com/whp/222723275"),
                    ts = ("121"),
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message=message
                )   

def welcome(event: VkLongPoll.DEFAULT_EVENT_CLASS, vk_api_method, longpoll):
    vk_api_method.messages.send(
                            keyboard=keyboards.welcome_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message='You are on welcome page of Test! Lets go? (GO! / exit)'
                            )
    
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
                send_menu(event, vk_api_method, message=f"Hi, {name}. Here is the main menu:")
                position='menu'
            
            # Menu
            elif position=='menu':
                if event.text == 'Profile':
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Your profile: {user}'
                    )
                    position='menu'
                    send_menu(event, vk_api_method)
                elif event.text == 'Tests':
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Lets start doing. We have some tests. Look!'
                    )
                    position = 'menu'
                    drive_test(event=event, user=user, vk_api_method=vk_api_method, longpoll=longpoll)
                    send_menu(event, vk_api_method)
                elif event.text == 'Statistic':
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Statistic: \n {user.get_statistic()}'
                    )
                    position='menu'
                    send_menu(event, vk_api_method)
                else:
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Command not found'
                    )
                    send_menu(event, vk_api_method)
            
            
                     
    vk_api_method.messages.send(
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message='Finishing all progress...'
                            )
    
    
    
