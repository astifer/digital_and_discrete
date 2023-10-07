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
        'name': [],
        'score': [],
        'time': []        
    }
    
    def __init__(self, user_id)->None:
        self.user_id = user_id
        
    def add_complit(self, test_name: str, score: float, time)->None:
        self.data['name'].append(test_name)
        self.data['score'].append(score)
        self.data['time'].append(time)
        logging.info(f"succesfully append test data [user_id:{self.user_id}]")
    
    def average_score_all(self)->float:
        if self.data['score']:
            res = sum(self.data['score'])/len(self.data['score'])
            return res
        else:
            return 0
        
    def get_all_stat(self)->pd.DataFrame:
        
        df = pd.DataFrame(self.data)
        df.to_csv('data/user_data.csv')
        
        fig = px.bar(df, x="name", y="time",title="Time statistic")
        fig.write_image('data/time_stat.jpeg')
        
        fig = px.bar(df, x="name", y="score",title="Score statistic")
        fig.write_image('data/score_stat.jpeg')
        
        return df
    