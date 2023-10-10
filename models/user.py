import enum
import random
import time

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from sklearn.metrics import accuracy_score


from models.content import all_tests
from models.statistic import Statistic

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)



class User():
    id: int
    name: str
    
    def __init__(self, id) -> None:
        
        self.id = id
        self.name = ''
        self.email = ''
        self.statistic = Statistic(self.id)
        
    def run_test(self, 
                 test_name: int, 
                 event: VkEventType, 
                 longpoll: VkLongPoll, 
                 vk_api_method)->None:
        
        logging.info(f"[user_id:{self.id}]  run {test_name}")
        score, elapased_time, good_info = all_tests[test_name].run(self.id, event=event, longpoll=longpoll, vk_api_method=vk_api_method)
        self.statistic.add_complit(test_name, score, elapased_time)

        return good_info
    
    def get_statistic(self):
        return self.statistic.get_all_stat()
    
    def save_plot(self):
        return
    
    def add_complete(self, test_name, score, time):
        self.statistic.add_complit(test_name=test_name, score=score, time=time)
        
    def __str__(self):
        
        result = f"\n Name: {self.name} \n Id: {self.id} \n Tests passed: {self.statistic.count}"
        return result
    

