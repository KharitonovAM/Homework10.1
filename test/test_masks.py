import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("data, result", [(13123, "**3123"), ("", "**")])
def test_get_mask_account(data, result):
    assert get_mask_account(data) == result


@pytest.mark.parametrize("data, result", [(1234567890123456, "1234 56** **** 3456")])
def test_get_mask_card_number(data, result):
    assert get_mask_card_number(data) == result


def test_get_mask_card_number1(make_rand_card_number):
    assert get_mask_card_number(make_rand_card_number)
