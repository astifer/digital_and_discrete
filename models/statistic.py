import random
import time

from vk_api.utils import get_random_id
from sklearn.metrics import accuracy_score
import pandas as pd
import plotly.express as px

from tools.settings import config
from models.content import all_tests
import models.keyboards as keyboards

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


    
class Statistic():
    data = {
        'Geography': {
            'score': [],
            'time': [] 
            },
        'Counting': {
            'score': [],
            'time': [] 
            },
        'Simple numbers': {
            'score': [],
            'time': [] 
            }
    }
    
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.count = 0
        
    def add_complit(self, test_name, score, time):
        self.count += 1
        self.data[test_name]['score'].append(score)
        self.data[test_name]['time'].append(time)
        
        users_data = pd.read_csv('data/users_data.csv')
        
        temp_df = pd.DataFrame({'user_id': self.user_id,
                                'test_name': test_name,
                                'score': score,
                                'time': -float(time)}, index=[0])
        
        updated_data = pd.concat([users_data, temp_df], ignore_index=True)
        updated_data.to_csv('data/users_data.csv', index=False)
        
        logging.info(f"[user_id:{self.user_id}] succesfully append test data")
        return True

    def average_each(self)->dict:
        info = {}
        for test_name in self.data:
            info[test_name] = 0
            if self.data[test_name]['score']:
                info+= f"{str(test_name)}: {sum(self.data[test_name]['score'])/len(self.data[test_name]['score']):.2f} \n"
            
        return info
    
    def get_all_stat(self)->pd.DataFrame:
        
        users_data = pd.read_csv('data/users_data.csv')
        if len(users_data)==0:
            logging.info(f'[user_id:{self.user_id}] empty stat')
            return False
        
        temp = users_data[users_data['user_id']==self.user_id]
        
        fig = px.line(data_frame=temp, x=[i for i in range(len(temp))], y="time",title="Time trajectory", markers=True, color='test_name')
        fig.write_image(f'data/{self.user_id}_time_stat.jpeg')
        
        fig = px.line(data_frame=temp, x=[i for i in range(len(temp))], y="score",title="Score trajectory", markers=True, color='test_name')
        fig.write_image(f'data/{self.user_id}_score_stat.jpeg')
        
        logging.info(f'[user_id:{self.user_id}] read and wrtie new stat')
        
        return True
    
    def get_all_mean(self)->pd.DataFrame:
        
        users_data = pd.read_csv('data/users_data.csv')
        if len(users_data)==0:
            logging.info(f'[user_id:{self.user_id}] empty stat')
            return False
        
        temp = users_data[users_data['user_id']==self.user_id]
        
        fig = px.line(data_frame=temp.groupby(['test_name']).mean().reset_index(), x=[i for i in range(len(temp))], y="time",title="Time statistic")
        fig.write_image(f'data/{self.user_id}_time_stat.jpeg')
        
        fig = px.line(data_frame=temp.groupby(['test_name']).mean().reset_index(), x=[i for i in range(len(temp))], y="score",title="Score statistic")
        fig.write_image(f'data/{self.user_id}_score_stat.jpeg')
        
        logging.info(f'[user_id:{self.user_id}] read and wrtie new stat')
        
        return True