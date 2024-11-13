from src.widget import mask_account_card
from src.widget import get_date


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(mask_account_card('счет 123232121323232'))
    print(mask_account_card('карта 123232121323232'))
    print(mask_account_card('счет 123232121323232'))
    print(get_date('11.08/2024'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
