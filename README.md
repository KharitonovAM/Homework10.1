# Блок домашних заданий по теме "Разработка на Python" 
## Краткое описание проекта

Иллюстрирует навыки полученные по теме углубленный GIt, представляет из себя наюор модулей:
+ masks модуль по работе с масками

	- get_mask_card_number
  Функция получает на входе номер карты, возвращает строковое значение где цифры разбиты в группы по 4 и все кроме первых 6-ти и последних 4-х цифрах карыты заменены на *
  - get_mask_account
  Функция получает на входе номер счета и возвращает ** и последние 4 цифры счета *

+ proctssing
  содержит 2 функции:
  - filter_by_state
  Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению
  - sort_by_date
  Возвращает список отсортированныц по параметру date, принимает необязательный параметр date_reverse


+ widget
  - mask_account_card
    Принимает номер карты или номер чсета и возвражает его под маской
  - get_date
    Изменяет формат даты
  

+ generators содержит 3 функции:
  - card_number_generator Выдает номера банковских карт в аданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров
  - transaction_descriptions Принимает список словарей с транзакциями и возвращает по очереди описание каждой операции
  - filter_by_currency Возвращет итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
  

+ decorators содержит декораторы
  - log Позволяет ввести логированиие функции, если в декоратор передать наименование файла, то логирование будет производиться в него. В противном случае данные удут печататься в терминале.


+ utils содержит утилиты, кторые позволяют работать с данными по транзакциями
  - get_amount_in_rub Принимает на вход информацию о транзакции, возвращает сумму транзакции в рублях
  - take_data_from_json принимает на вход путь до JSON-файла возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден, возвращает пустой список


+ external_api
  - get_exchange:
    Принимает на вход сумму и валюту, возвращает информацию по конверсии в соответствии с текущим курсом, данные получает по Api
## Установка и использование
### Требования к окружению

Для использования программы требуется установить на компьютер python v 3.8 и выше

### Установка проекта

Склонировать репозиторий:

       

       'git clone https://github.com/KharitonovAM/Homework10.1'

     

Создать и активировать виртуальное окружение:

       ```

       python -m venv venv

       source venv/bin/activate  # или venv\Scripts\activate для Windows

       ```
Установить зависимости

       ```

        pip install -r requirements.txt

       ```
Запуск проекта

       ```

        python manage.py runserver

       ```

## Примеры использования


Ниже рассматриваются примеры исполььзования некоторых функций

       ```
      test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

      filter_by_state(test_list)
       ```

По умолчанию отфильтровыет словари, в которых state = 'EXECUTED' и возвращает значение:

    ''' 
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    '''

Можно задать собственный фильтр во второй переменной:

    '''
    filter_by_state(test_list, 'CANCELED')
    '''

Вернёт список со словарями, где 'state' = 'CANCELED'

    '''
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]'
    '''

Формирование списка новых карт с применением зуданного диапазона

Этот функционал реализован в функции 

    '''
    card_number_generator(start_data:int,end_data:int)->list[str]

    for card_number in card_number_generator(1, 5):
    print(card_number)

    0000 0000 0000 0001 
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
    '''
## Документация и ссылки

Шаблон файла .env с инструкциями по использованию Api содержится в файле .env.simple 

Ссылки на описания работы функций можно получить используя функцию help 

    '''
    help(name_of_function)
    '''
## Тестирование
Для тестирования работы функций используйте pytest, все функции применяемые для тестирования, находятся в директрии /test

Все функции в программе протестированы на выполнение заданного функционала.
Для автоматическго тестирования использовались фикструры. содержащиеся в файле .conftest.py
Для вызова тестирования можно использовать команды

    '''
    pytest
    pytest --cov
    '''
тесты покрывают 100% написанного кода
## Лицензия
Python Software Foundation License (PSFL)
