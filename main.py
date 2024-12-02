from src.widget import mask_account_card
from src.widget import get_date
from src.processing import sort_by_date
from src.generators import transaction_descriptions, filter_by_currency
from src.decorators import log

z = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

if __name__ == '__main__':
    '''
    print(mask_account_card('счет 123232121323232'))
    print(mask_account_card('карта 123232121323232'))
    print(mask_account_card('счет 123232121323232'))
    print(get_date('11.08/2024'))

    k = filter_by_currency(z,'USD')
    print(next(k))
    print(next(k))
'''
    l = transaction_descriptions(z)
    print(next(l))
    print(next(l))

@log()
def my_summ(a, b, c):
    return a+b+c

z = my_summ(1,1,'u')
