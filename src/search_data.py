import json
from typing import Any
import re
from collections import Counter


def search_transaction_by_string(
    list_transactions: list[dict[Any:Any]], searching_string: str
) -> list[dict[Any:Any]]:
    """Функция получает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка."""
    result_list = [
        find_dict
        for find_dict in list_transactions
        if re.findall(searching_string, find_dict["description"])
    ]
    return result_list


def make_dict_category(list_dict, list_category):
    """Функция принимает списко словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи - названия категорий, a значения — это количество операций в каждой категории
    """

    my_list = []
    for operation in list_dict:
        if "description" in operation.keys():
            for item in list_category:
                if item in operation["description"]:
                    my_list.append(item)

    return Counter(my_list)
