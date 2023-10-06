import random
from tests.models import Test
from settings import config

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

      
     
test_a = Test(
    name="Geography",
    description="Check your geography knowledge",
    questions=['1) How long is equator?',
               '2) Where do polar bears live?',
               '3) How many continents are on our planet?',
               '4) How many oceans are on our planet?',
               '5) The radius of the earth is approximately equal to ... km',
               '6) Which country on the map looks like a boot?',
               '7) The land of the rising sun',
               '8) Red flag with moon and star',
               '9) Where does the kangaroo live?',
               '10) The largest continent'
               ],
    possible_answers=[
        ['23 km', '40000 km', '40000 m','82 inch'],
        ['Arctic', 'Africa', 'Antarctic', 'China'],
        ['3', '7', '6', '5'],
        ['4', '5', '6', '7'],
        ['7800', '2100', '4500', '6300'],
        ['Germany', 'France', 'Italy', 'China'],
        ['China', 'Japan', 'Maroco', 'Brazil'],
        ['Turkey', 'Africa', 'Australia', 'Tunisia'],
        ['Australia', 'Africa', 'Tunisia', 'Turkey'],
        ['South America', 'Africa', 'Eurasia', 'Australia']
        ],
    actual_answers = [1, 0, 2, 1, 3, 2, 1, 0, 0, 2]
)

test_a.description=f'\n {test_a.name} {test_a.id}\n This is a simple quizz about geography. If you know smth about our Earth, click start!'

test_b = Test(
    name="Counting",
    description="Check your counting abilities",
    questions=['1) 12 + 34 + 76',
               '2) 37 - 22 - 35',
               '3) 333 / 3 + 8',
               '4) 6^3',
               '5) sqrt(144)',
               '6) 4! ',
               '7) 66 / 11 * 11',
               '8) sqrt(625)',
               '9) 2^10',
               '10) 3^4'
               ],
    possible_answers=[
        ['120', '122', '118','121'],
        ['-20', '-18', '-19', '-21'],
        ['118', '123', '119', '120'],
        ['36', '216', '18', '60'],
        ['144', '8', '14', '12'],
        ['10', '42', '24', '6'],
        ['111', '66', '11', '666'],
        ['25', '5', '15', '35'],
        ['1024', '128', '2048', '512'],
        ['9', '243', '81', '27']
        ],
    actual_answers = [1, 0, 2, 1, 3, 2, 1, 0, 0, 2]
)

test_b.description=f'\n {test_b.name} {test_b.id}\n This is a simple quizz for counting. Be attentive, click start!'

test_c = Test(
    name="Simple numbers",
    description="Check your knowladge about simple numbers",
    questions=['1) Find a simple number',
               '2) Find a simple number',
               '3) Find a simple number',
               '4) Find a simple number',
               '5) Find a simple number',
               '6) Find a simple number',
               '7) Find a simple number',
               '8) Find a simple number',
               '9) Find a simple number',
               '10) Find a simple number'
               ],
    possible_answers=[
        ['120', '113', '118','123'],
        ['67', '68', '69', '66'],
        ['118', '110', '109', '120'],
        ['60', '59', '62', '63'],
        ['50', '49', '48', '47'],
        ['42', '44', '43', '46'],
        ['99', '97', '98', '96'],
        ['239', '240', '236', '238'],
        ['131', '132', '136', '130'],
        ['994', '996', '991', '992']
        ],
    actual_answers = [1, 0, 2, 1, 3, 2, 1, 0, 0, 2]
)

test_c.description=f'\n {test_c.name} {test_c.id}\n This is a simple quizz for fiding simple numbers. Be attentive, click start!'


all_tests = {
    test_a.name: test_a,
    test_b.name: test_b,
    test_c.name : test_c
}

all_tests_desription = f"{test_a.description} \n {test_b.description} \n {test_c.description}"