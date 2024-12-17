import csv
from typing import Any

import pandas as pd


def take_transactions_from_csv(filename: str) -> list[dict[Any, Any]]:
    """Функция для считывания финансовых операций из CSV файла.
    Принимает на вход наименование файла в str,
    возвращает список из словарей с транзакциями"""
    with open(filename, encoding="utf-8") as f:
        data = csv.DictReader(f, delimiter=";")
        data_list = [row for row in data]
    return data_list


def take_transactions_from_exel(filename: str) -> list[dict[Any, Any]]:
    """ "Функция для считывания финансовых операций из EXEL файла.
    Принимает на вход наименование файла в str,
    возвращает список из словарей с транзакциями"""
    exel_data = pd.read_excel(filename)
    return exel_data.to_dict("records")
