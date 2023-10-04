import random
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

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
        
        logging.info(" test created")
        
    def run(user_id):
        pass
    
    def get_stat():
        pass
    
    
    
test_a = Test(
    name="Nature",
    description="",
    questions=['How long is equator?',
               'Where do polar bears live?',
               ],
    possible_answers=[
        ['23 km', '40000 km', '40000 m','82 inch'],
        ['Arctic', 'Africa', 'Antarctic', 'China'],
        ],
    actual_answers = [1,0]
)

