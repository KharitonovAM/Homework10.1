from typing import Any, Generator


def filter_by_currency(
    transactions_list: list[dict[Any, Any]], currency: str
) -> filter[dict[Any, Any]]:
    """Возвращет итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    return filter(
        lambda transaction: transaction["operationAmount"]["currency"]["name"]
        == currency,
        transactions_list,
    )


def transaction_descriptions(transactions: list[dict[Any, Any]]) -> Generator[str]:
    """принимает список словарей с транзакциями и возвращает по очереди описание каждой операции"""
    return (x["description"] for x in transactions)


def card_number_generator(start_data: int, end_data: int) -> list[str]:
    """выдает номера банковских карт в аданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров"""
    if start_data < 1 or end_data > 9999999999999999 or start_data >= end_data:
        raise ValueError("Введите корректные значения")
    kard_number = [
        "0" * (16 - len(str(i))) + str(i) for i in range(start_data, end_data + 1)
    ]
    return [
        " ".join([item[index - 4 : index] for index in range(4, 17, 4)])
        for item in kard_number
    ]
