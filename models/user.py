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
    
    def __init__(self, id) -> None:
        
        self.id = id
        self.name = ''
        self.email = ''
        self.statistic = Statistic(self.id)
        
    def run_test(self, test_name: int, event: VkEventType, longpoll: VkLongPoll, vk_api_method)->None:
        logging.info(f"{self.name} run {test_name}")
        score, elapased_time = all_tests[test_name].run(self.id, event=event, longpoll=longpoll, vk_api_method=vk_api_method)
        self.statistic.add_complit(test_name, score, elapased_time)
    
    def get_statistic(self):
        info = self.statistic.get_all_stat()
        return info
    
    def __str__(self):
        
        result = f"\n Name: {self.name} \n Id: {self.id} \n Email: {self.email}"
        return result
    

