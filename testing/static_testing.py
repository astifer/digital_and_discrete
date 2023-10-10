import pytest

from models.user import User
from models.statistic import Statistic
from models.testik import Test

@pytest.fixture
def user():
    user = User(4000)
    user.name = "Artem"
    return user

@pytest.fixture
def statistic():
    return Statistic(4000)

@pytest.fixture
def test():
    return Test('Math', 'lalala', [' '], [' '], [' '], [' '])



def test_user_str_1(user):
    n = user.name
    
    assert n == "Artem"

def test_statistic_add_complit(statistic):
    # Add your test logic for add_complit() here
    pass

def test_statistic_average_score_all(statistic):
    # Add your test logic for average_score_all() here
    pass

def test_statistic_get_all_stat(statistic):
    # Add your test logic for get_all_stat() here
    pass

def test_test_get_stat(test):
    # Add your test logic for get_stat() here
    pass