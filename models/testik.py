import enum
import random
import time

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from sklearn.metrics import accuracy_score

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

from tools.settings import config
from tools.utils import send_mess, send_mess_kb
import models.keyboards as keyboards

class Test():
    index2letter: dict  = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
    }
    
    letter2index: dict  = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
    }
    
    def __init__(self, name, description, questions, possible_answers, actual_answers, links) -> None:
        self.name = name
        self.id = random.randint(0,10000)
        self.description = description
        self.links = links
        
        if len(questions)==len(possible_answers) and len(possible_answers)==len(actual_answers):
            self.questions = questions
            self.possible_answers = possible_answers
            self.actual_answers = actual_answers
        else:
            raise Exception("Lenghts do not match")
        
        logging.info(f"test {self.name} created")
        
    def run(self, user_id, event: VkEventType, longpoll: VkLongPoll, vk_api_method):
        user_answers = [0]*10
        position=0
        start_time = time.time()
        
        send_mess_kb(event=event, vk_api_method=vk_api_method, 
                     keyboard=keyboards.test_keyboard,
                     message=f"Lets go!\n {self.questions[position]} \n {self.parse_pa(self.possible_answers[position])}")
        
        
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                
                if event.text in self.letter2index:
                    
                    user_answers[position] = self.letter2index[event.text]
                    position+=1
                    
                if position == 10:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    form_time = '%.2f' % elapsed_time
                    score = accuracy_score(self.actual_answers, user_answers)
                    good_info = self.src_errors(user_answers)
                    
                    logging.info(f'[user_id:{user_id}] score: {score}, time: {form_time}')
                    break
                
                send_mess_kb(event=event, vk_api_method=vk_api_method, 
                             keyboard=keyboards.test_keyboard,
                             message = self.questions[position] + "\n" +self.parse_pa(self.possible_answers[position]))
                
        
        send_mess_kb(event=event, vk_api_method=vk_api_method, 
                  keyboard=keyboards.test_keyboard,
                  message=f"Your score is {score}, time: {form_time}") 
        

        return score, form_time, good_info
          
    def parse_pa(self, list_of_a: list)->str:
        result = ''
        for i in range(4):
            result += self.index2letter[i] + " : "
            result += list_of_a[i] + "\n"
            
        return result
    
    
    def src_errors(self, ges):
        errors = []
        info ='Your errors: \n'
        
        for i in range(len(self.actual_answers)):

            if ges[i] != self.actual_answers[i]:
                errors.append(i) 
        
        for ind in errors:
            info += f"{ind+1}. {self.links[ind]} \n"
        
        if len(errors)==0:
            return ''
        return info
    
