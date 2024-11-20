from src.widget import mask_account_card
from src.widget import get_date
from src.processing import sort_by_date
from src.generators import filter_by_currency

test =  [{
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
       }
]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(mask_account_card('счет 123232121323232'))
    print(mask_account_card('карта 123232121323232'))
    print(mask_account_card('счет 123232121323232'))
    print(get_date('11.08/2024'))



    q = filter_by_currency(test,'USD')
    for i in range(1):
        print(next(q))

    print(next(q))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
