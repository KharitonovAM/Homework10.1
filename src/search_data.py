import json
from typing import Any
import re

def search_transaction_by_string(list_transactions:list[dict[Any:Any]], searching_string:str)->list[dict[Any:Any]]:
    '''Функция получает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.'''
    result_list =[find_dict for find_dict in list_transactions if re.findall(searching_string, find_dict['description'])]
    return result_list


