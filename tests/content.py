import random
from models.test import Test

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

      
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

test_a.description=f'\n {test_a.name} {test_a.id}\n This is a simple quizz abuot nature. If you know smth about our Earth, click start!'




all_tests_desription =f"{test_a.description} \n {None}"