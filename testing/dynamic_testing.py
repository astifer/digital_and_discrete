import pytest
from vk_api.longpoll import VkEventType, VkLongPoll

from main import longpoll, vk

def test_type_longpoll():
    assert type(longpoll) == VkLongPoll
