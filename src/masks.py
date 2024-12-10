import logging
from typing import Union

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(name)s - %(message)s',
                    filename='../logs/utils.log',
                    filemode='w')

masks_logging_card = logging.getLogger("masks_logging")
masks_logging_account = logging.getLogger('mask_account')


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция получает на входе номер карты,
    возвращает строковое значение где цифры разбиты в группы по 4 и все
    кроме первых 6-ти и последних 4-х цифрах карыты заменены на *"""
    masks_logging_card.debug("Запуск функции  get_mask_card_number")

    mask_card = []
    number_card = str(number_card)
    number_card_asterix = ""
    masks_logging_card.debug("Переходим к обработке номера карты get_mask_card_number")
    for number in number_card:
        if (
            len(number_card_asterix) < 6
            or len(number_card_asterix) > len(number_card) - 5
        ):
            number_card_asterix += number
        else:
            number_card_asterix += "*"
    start_index_of_interval = 0
    masks_logging_card.debug("Завершена обработка номера карты get_mask_card_number")
    masks_logging_card.debug("Переходи к разбивке по блокам по 4 цифры в get_mask_card_number")
    for index in range(0, len(number_card_asterix) + 1, 4):
        mask_card.append(number_card_asterix[start_index_of_interval:index])
        start_index_of_interval = index
    masks_logging_card.info('Это блок инфо')
    masks_logging_card.debug("Завершание работы функции get_mask_card_number")
    return " ".join(mask_card[1:])


def get_mask_account(accaut_number: Union[int, str]) -> str:
    """Функция получает на входе номер счета и
    возвращает ** и последние 4 цифры счета *"""
    masks_logging_account.debug("Функция get_mask_account")
    return "**" + str(accaut_number)[-4:]
