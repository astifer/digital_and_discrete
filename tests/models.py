import enum
import random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from settings import config
from content import test_a, test_b, test_c, all_tests, all_tests_desription
import keyboards

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class Test():
    q_map: dict  = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
    }
    
    def __init__(self, name, description, questions, possible_answers, actual_answers) -> None:
        self.name = name
        self.id = random.randint(0,10000)
        self.description = description
        
        if len(questions)==len(possible_answers) and len(possible_answers)==len(actual_answers):
            self.questions = questions
            self.possible_answers = possible_answers
            self.actual_answers = actual_answers
        else:
            raise Exception("Lenghts do not match")
        
        logging.info("test created")
        
    def run(self, user_id, event: VkEventType, longpoll: VkLongPoll, vk_api_method):
        user_answers = []
        position=0
        
        vk_api_method.messages.send(
                            keyboard=keyboards.test_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message=f"Время пошло!\n {self.questions[position]}"
                            )
        
        logging.info(f'user starts test {self.name}')
        
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                
                user_answers[position] = event.text
                logging.info(f'user {position }answer is {event.text}')
                
                vk_api_method.messages.send(
                                keyboard=keyboards.test_keyboard.get_keyboard(),
                                key= (config.keyboard_key),
                                server= ("https://lp.vk.com/whp/222723275"),
                                ts = ("121"),
                                user_id = event.user_id,
                                random_id = get_random_id(),
                                message=self.questions[position]
                                )
                position+=1
                    
                    
    def get_stat(self):
        pass
    


class User():
    
    def __init__(self, id) -> None:
        
        self.id = id
        self.name = ''
        self.email = ''
        self.statistic = None
        
    def run_test(self, test_name: int)->None:
        logging.info(f"{self.name} run {test_name}")
        all_tests[test_name].run(self.id)
        
    
    
    def get_statistic(self)->list:
        return
    
    
    def __str__(self):
        
        result = f"\n Name: {self.name} \n Id: {self.id} \n Email: {self.email}"
        return result
    
