import json
import logging

from src.external_api import get_exchange, take_summ_in_ruble

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(name)s - %(message)s',
                    filename='../logs/utils.log',
                    filemode='w')

utils_logging = logging.getLogger("utils_logging")


def take_data_from_json(to_json_file="../data/operations.json"):
    """принимает на вход путь до JSON-файла возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден, возвращает пустой список"""

    utils_logging.debug("Запустилась функция take_data_from_json")
    try:
        with open(to_json_file, encoding="utf-8") as f:
            utils_logging.debug("Получили данные из файла")
            data = json.load(f)
    except FileNotFoundError:
        utils_logging.error("файл не найден")
        data = []
    if isinstance(data, list) is False:
        utils_logging.error("Тип переменной не список")
        data = []
    return data


def get_amount_in_rub(transaction):
    """Принимает на вход информацию о транзакции, возвращает сумму транзакции в рублях"""

    utils_logging.debug("Запустилась функция")
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    utils_logging.debug("Получили данные по валюте и сумме")
    if currency_code != "RUB":
        utils_logging.debug("Валюта не рубль, работает программа")
        return take_summ_in_ruble(get_exchange(amount, currency_code))
    else:
        utils_logging.debug("Валюта рубль, возвращаем данные")
        return amount
