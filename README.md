# Домашняя работа 10-1
## Краткое описание проекта

Иллюстрирует навыки полученные по теме углубленный GIt, представляет из себя наюор модулей:
+ masks
модуль по работе с масками
содержит 2 функции:
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

'''
test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

filter_by_state(test_list)
'''

По умолчанию отфильтровыет словари, в которых state = 'EXECUTED' и возвращает значение:

'[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
'

Можно задать собственный фильтр во второй переменной:

'''
filter_by_state(test_list, 'CANCELED')
'''

Вернёт список со словарями, где 'state' = 'CANCELED'

'[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]'

## Документация и ссылки

Ссылки на описания работы функций можно получить используя функцию help 

'''
help(name_of_function)
'''

## Лицензия
Python Software Foundation License (PSFL)
