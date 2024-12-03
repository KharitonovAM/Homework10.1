import json

def take_data_from_json(to_json_file = '../data/operations.json' ):
    '''принимает на вход путь до JSON-файла возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден, возвращает пустой список'''

    try:
        with open(to_json_file, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    if isinstance(data, list) is False:
        data = []
    return data
