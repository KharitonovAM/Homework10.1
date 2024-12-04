import json
from unittest.mock import Mock

from src.external_api import get_exchange, take_summ_in_ruble


def take_data_from_json(to_json_file="../data/operations.json"):
    """принимает на вход путь до JSON-файла возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден, возвращает пустой список"""

    try:
        with open(to_json_file, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    if isinstance(data, list) is False:
        data = []
    return data


def get_amount_in_rub(transaction):
    """Принимает на вход информацию о транзакции, возвращает сумму транзакции в рублях"""
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency_code != "RUB":
        return take_summ_in_ruble(get_exchange(amount, currency_code))
    else:
        return amount
