def filter_by_state(list_of_dict:dict, state:str = 'EXECUTED')->list:
    '''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению'''
    return [x for x in list_of_dict if x['state']==state]
