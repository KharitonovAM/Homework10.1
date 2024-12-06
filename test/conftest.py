import random

import pytest


@pytest.fixture
def make_rand_card_number():
    return random.randint(999999999999999, 9999999999999999)


@pytest.fixture
def make_generator_filter_list():
    return [
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
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def make_long_generator_filter_list():
    return [
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
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "BYN", "code": "BYN"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "RUS", "code": "RUS"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def card_dannie_info():
    return [
        [1, 5],
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ],
    ]


@pytest.fixture
def string_data():
    return ["testfile.json", '"string1=some_data"']


@pytest.fixture
def database_from_api():
    return {"info": ["data1", "info2", "info3"], "result": 100000}


@pytest.fixture
def dict_rub():
    return [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612",
        },
        "97853.86",
    ]


@pytest.fixture
def dict_usd():
    return {
        "operationAmount": {
            "amount": "97853.86",
            "currency": {"name": "USD.", "code": "USD"},
        }
    }
