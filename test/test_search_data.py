import pytest
from src.search_data import make_dict_category, search_transaction_by_string


def test_search_transaction_by_string(make_generator_filter_list):
    assert search_transaction_by_string(make_generator_filter_list, "организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_search_transaction_by_string_mistake(make_generator_filter_list):
    with pytest.raises(TypeError):
        search_transaction_by_string(make_generator_filter_list)


def test_make_dict_category(make_generator_filter_list):
    assert make_dict_category(
        make_generator_filter_list, ["Перевод со счета на счет", "Перевод организации"]
    ) == {"Перевод со счета на счет": 1, "Перевод организации": 1}
