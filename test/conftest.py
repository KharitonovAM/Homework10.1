import random

import pytest


@pytest.fixture
def make_rand_card_number():
    return random.randint(999999999999999, 9999999999999999)
