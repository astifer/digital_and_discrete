import random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

import keyboards
from settings import config
from models import User
from tests.content import * 

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
                            message=all_tests_desription
                            )
    
    position='test_choice'
    for event in longpoll.listen():
        
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            if position=='test_choice' and event.text in all_tests:
                test_id = all_tests[event.text].id
                user.run_test(test_id=test_id)
                position = 'test done'
                
            elif position=='test_choice' and event.text == 'exit':
                break
            else:
                break


def welcome(event: VkLongPoll.DEFAULT_EVENT_CLASS, vk_api_method, longpoll):
    vk_api_method.messages.send(
                            keyboard=keyboards.welcome_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message='You are on welcome page of Test! Lets go?'
                            )
    
    position='start'
    user = User(event.user_id)
    
    for event in longpoll.listen():
        
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            if event.text == 'exit':
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
                
                vk_api_method.messages.send(
                    keyboard=keyboards.menu_keyboard.get_keyboard(),
                    key= (config.keyboard_key),
                    server= ("https://lp.vk.com/whp/222723275"),
                    ts = ("121"),
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message=f'Nice to meet you, {name}. Here is the main menu'
                )
                position='menu'
            
            # Menu
            elif position=='menu':
                if event.text == 'Profile':
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Your profile: {user}'
                    )
                    position='profile'
                elif event.text == 'Tests':
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Lets start doing. We have some tests. Look!'
                    )
                    position = 'tests'
                    drive_test(event=event, user=user, vk_api_method=vk_api_method, longpoll=longpoll)
                elif event.text == 'Statistic':
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Statistic: '
                    )
                    position='statistic'
                else:
                    vk_api_method.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message=f'Command not found'
                    )
                    
            elif position=='profile':
                return
                
            elif position=='tests':
                
                return
            
            elif position=='statistic':
                
                return
                
                     
    vk_api_method.messages.send(
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message='Finishing all progress...'
                            )
    
    
    
