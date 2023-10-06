import enum
import random
import time

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from sklearn.metrics import accuracy_score

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

from tools.settings import config
import models.keyboards as keyboards

class Test():
    q_map: dict  = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
    }
    
    q_map_l: dict  = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
    }
    statistic: {
        'acc': [],
        'tm': [],
    }
    
    def __init__(self, name, description, questions, possible_answers, actual_answers) -> None:
        self.name = name
        self.id = random.randint(0,10000)
        self.description = description
        self.statistic = {
        'acc': [],
        'tm': [],
    }
        
        if len(questions)==len(possible_answers) and len(possible_answers)==len(actual_answers):
            self.questions = questions
            self.possible_answers = possible_answers
            self.actual_answers = actual_answers
        else:
            raise Exception("Lenghts do not match")
        
        logging.info("test created")
        
    def run(self, user_id, event: VkEventType, longpoll: VkLongPoll, vk_api_method):
        user_answers = [0]*10
        position=0
        start_time = time.time()
        
        vk_api_method.messages.send(
                            keyboard=keyboards.test_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message=f"Lets go!\n {self.questions[position]} \n {self.parse_pa(self.possible_answers[position])}"
                            )
        
        logging.info(f'user starts test {self.name}')
        
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                
                logging.info(f'user {position} answer is {event.text}')
                user_answers[position] = self.q_map_l[event.text]
                
                position+=1
                
                if position == 10:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    form_time = '%.2f' % elapsed_time
                    score = accuracy_score(self.actual_answers, user_answers)
                    logging.info(f'score: {score}, time: {form_time}')
                    break
                
                mess = self.questions[position] + "\n" +self.parse_pa(self.possible_answers[position])
                vk_api_method.messages.send(
                                keyboard=keyboards.test_keyboard.get_keyboard(),
                                key= (config.keyboard_key),
                                server= ("https://lp.vk.com/whp/222723275"),
                                ts = ("121"),
                                user_id = event.user_id,
                                random_id = get_random_id(),
                                message=mess
                                )
                
        
        vk_api_method.messages.send(
                            keyboard=keyboards.test_keyboard.get_keyboard(),
                            key= (config.keyboard_key),
                            server= ("https://lp.vk.com/whp/222723275"),
                            ts = ("121"),
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message=f"Your score is {score}, time: {form_time}"
                            ) 
        
        self.statistic['acc'].append(score)
        self.statistic['tm'].append(form_time)
        
        return score, form_time    
          
    def parse_pa(self, list_of_a: list)->str:
        result = ''
        for i in range(4):
            result += self.q_map[i] + " : "
            result += list_of_a[i] + "\n"
            
        return result
    
    def get_stat(self):
        '''
        list with result anybody passed this test
        '''
        
        return self.statistic