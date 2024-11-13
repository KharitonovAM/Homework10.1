import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "date, result",
    [
        ("счет 123123123111", "счет **3111"),
        ("карта 1234567890123456", "карта 1234 56** **** 3456"),
    ],
)
def test_mask_account_card(date, result):
    mask_account_card(date) == result


def test_mask_account_card1():
    assert mask_account_card("счет 56455455656565465465465654") == "счет **5654"

    with pytest.raises(IndexError):
        assert mask_account_card("счет56455455656565465465465654")


@pytest.mark.parametrize(
    "data,result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-10-18T02:26:18.671407", "18.10.2024"),
    ],
)
def test_get_date(data, result):
    get_date(data) == result
