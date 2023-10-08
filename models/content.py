import random
from models.testik import Test
import pandas as pd
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

user_manual = "Hello! This is simple bot Cradm Lozzer. What I can do? I have a few start command: \n"
user_manual += "wikipedia - find info about subject, you write past command \n"
user_manual += "weather - check the weather in city, you write past command \n"
user_manual += "tests - a whole game with interesting quizzes and statistic! \n"
user_manual += "echo - default command"

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
    actual_answers = [1, 0, 2, 1, 3, 2, 1, 0, 0, 2],
    links = ['https://en.wikipedia.org/wiki/Equator',
             'https://www.wwf.org.uk/learn/wildlife/polar-bears',
             'https://ru.wikipedia.org/wiki/Континент',
             'https://en.wikipedia.org/wiki/Ocean',
             'https://en.wikipedia.org/wiki/Earth_radius#:~:text=A%20nominal%20Earth%20radius%20is,km)%20for%20the%20following%20reasons',
             'https://teacherscollegesj.org/which-country-is-known-as-the-boot/#:~:text=One%20of%20the%20most%20identifiable,bordered%20by%20the%20Tyrrhenian%20Sea',
             'https://www.jluggage.com/blog/japan/why-is-japan-called-land-of-rising-sun/#:~:text=Japan-the%20Land%20of%20the%20Rising,mean%20“where%20the%20sun%20rises”',
             'https://www.edarabia.com/turkey/flag/',
             'https://misfitanimals.com/kangaroos/where-do-kangaroos-live/#:~:text=Kangaroos%20Natural%20Habitat.%20Kangaroos%20are,of%20the%20continent%20over%20time',
             'https://en.wikipedia.org/wiki/Asia#:~:text=Asia%20is%20the%20largest%20continent,coastline%2C%20at%2062%2C800%20kilometres%20(39%2C022%C2%A0mi)'
             ]
)

test_a.description=f'{test_a.name}\n This is a simple quizz about geography. If you know smth about our Earth, click start!'

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
    actual_answers = [1, 0, 2, 1, 3, 2, 1, 0, 0, 2],
    links = ['https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/',
             'https://calculator888.ru/'
             ]
)

test_b.description=f'{test_b.name} \n This is a simple quizz for counting. Be attentive, click start!'

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
    actual_answers = [1, 0, 2, 1, 3, 2, 1, 0, 0, 2],
    links = ['http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php',
             'http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php'
             ]
)

test_c.description=f'{test_c.name}\n This is a simple quizz for fiding simple numbers. Be attentive, click start!'


all_tests = {
    test_a.name: test_a,
    test_b.name: test_b,
    test_c.name : test_c
}

all_tests_desription = f"{test_a.description} \n {test_b.description} \n {test_c.description}"

logging.info('tests created')

users_data = pd.DataFrame(columns=['user_id','test_name','score','time'])
users_data.to_csv('data/users_data.csv', index=False)

logging.info('users table created')
