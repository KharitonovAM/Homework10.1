import os
from unittest.mock import patch

import pytest

import src.utils
from src.utils import get_amount_in_rub, take_data_from_json


def test_with_bad_filename():
    assert take_data_from_json("file_with_bad_name.sfasfasf") == []


@pytest.mark.parametrize(
    "filename, rezult", [("test.json", []), ("asfasfasdf.json", [])]
)
def test_empy_file(filename, rezult):
    temp_file = open(filename, "a", encoding="utf-8")
    temp_file.write('""')
    temp_file.close()
    my_result = take_data_from_json(filename)
    os.remove(filename)
    assert my_result == rezult


def test_empty_file_2():
    temp_file = open("test.json", "a", encoding="utf-8")
    temp_file.write('" "')
    temp_file.close()
    z = take_data_from_json("test.json")
    os.remove("test.json")
    assert z == []


def test_not_list_result(string_data):
    assert take_data_from_json(string_data[0]) == []


def test_get_amount_to_ruble(dict_rub):
    assert get_amount_in_rub(dict_rub[0]) == dict_rub[1]


@patch("src.utils.get_exchange")
def test_mock_get_amount_in_rub(moke_exchange):
    moke_exchange.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1733334184, "rate": 105.005506},
        "date": "2024-12-04",
        "result": 863289.116863,
    }
    assert (
        src.utils.take_summ_in_ruble(src.utils.get_exchange(13123, "usd"))
        == 863289.116863
    )
