import enum
import random
import logging


class Test():
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
        
    def run(user_id):
        pass
    
    def get_stat():
        pass
    


class User():
    
    def __init__(self, id) -> None:
        
        self.id = id
        self.name = ''
        self.email = ''
        self.statistic = None
        
    def run_test(self,test_id: int)->None:
        pass
    
    
    def get_statistic(self)->list:
        pass
    
    
    def __str__(self):
        
        result = f"\n Name: {self.name} \n Id: {self.id} \n Email: {self.email}"
        return result
    