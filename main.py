from src.processing import filter_by_state, sort_by_date
from src.take_transaction_by_pb import take_transactions_from_csv, take_transactions_from_exel
from src.generators import filter_by_currency
from src.utils import take_data_from_json
from src.search_data import search_transaction_by_string
from src.widget import get_date, mask_account_card


def main()->None:
    '''Программа для взаимодействия с пользователем, позволяет пользователю
    определить откуда полуичить данные, отсортировать по дате, и отфильтровать
    по российскому рублю и произвольному слову, которое пользователь вводит сам
    возвращает '''
    list_status = ['EXECUTED', 'CANCELED', 'PENDING']

    list_file ={'1':'JSON-файл', '2':'CSV-файл', '3':'XLSX-файл'}
    file_name_dict = {'JSON-файл':'data/operations.json', 'CSV-файл':'data/transactions.csv', 'XLSX-файл': 'data/transactions_excel.xlsx'}
    start_text = '''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    '''
    type_file = input(start_text)
    if type_file not in list_file.keys():
        print('Вы сделали не правильный выбор, извините, работа программы прервана')
    else:
        print(f'Для обработки выбран {list_file[type_file]}')
        if type_file == '1':
            data_list = take_data_from_json(file_name_dict[list_file[type_file]])
        if type_file == '2':
            data_list = take_transactions_from_csv(file_name_dict[list_file[type_file]])
        if type_file == '3':
            data_list = take_transactions_from_exel(file_name_dict[list_file[type_file]])

        filter_status = ''
        while filter_status.upper() not in list_status:
            filter_status = input('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''')
            if filter_status.upper() not in list_status:
                print(f'Статус операции {filter_status} недоступен.')
        data_list = filter_by_state(data_list, filter_status.upper())
        print(f'Операции отфильтрованы по статусу "{filter_status}"')

        sort_data = input('Отсортировать операции по дате? Да/Нет\n')

        if sort_data.upper() == 'ДА':
            date_reverse = input('Отсортировать по возрастанию или по убыванию?\n')
            if date_reverse.upper() == 'ПО УБЫВАНИЮ':
                data_list = sort_by_date(data_list, True)
            else:
                data_list = sort_by_date(data_list)

        only_rub = input('Выводить только рублевые тразакции? Да/Нет\n')
        if only_rub.upper() == 'ДА':
            data_list = filter_by_currency(data_list,'RUB')

        word_description = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
        if word_description.upper() == 'ДА':
            word_description = input('Введите слово, по которому выполнить фильтрацию:\n')
            data_list = search_transaction_by_string(data_list, word_description)
        if len(data_list) == 0:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        else:
            print(f'Всего банковских операций в выборке: {len(data_list)}\n')

            for item in data_list:
                try:
                    print(f'{get_date(item['date'])} {item['description']}')
                    print(f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}')
                    print(f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n')
                except:
                    continue








if __name__ == '__main__':
    main()
