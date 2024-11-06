def filter_by_state(list_of_dict: dict, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    return [x for x in list_of_dict if x["state"] == state]


def sort_by_date(list_of_dict: dict, date_reverse: bool = False) -> list:
    """Возвращает список отсортированныц по параметру date, принимает необязательный параметр date_reverse"""
    return sorted(list_of_dict, key=lambda x: x["date"], reverse=date_reverse)
