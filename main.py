from src.widget import mask_account_card
from src.widget import get_date
from src.processing import sort_by_date
from src.generators import filter_by_currency


if __name__ == '__main__':
    print(mask_account_card('счет 123232121323232'))
    print(mask_account_card('карта 123232121323232'))
    print(mask_account_card('счет 123232121323232'))
    print(get_date('11.08/2024'))
