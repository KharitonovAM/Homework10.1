import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_generators_filter(make_generator_filter_list):
    temp_filter = filter_by_currency(make_generator_filter_list,'USD')
    test_list = []
    for i in range(2):
        test_list.append(next(temp_filter))
    assert test_list == make_generator_filter_list


def test_generatore_erise(make_generator_filter_list):
    temp_filter = filter_by_currency(make_generator_filter_list, 'USD')
    with pytest.raises(StopIteration):
        for i in range(4):
            next(temp_filter)


def test_generators_filter_with_four(make_generator_filter_list, make_long_generator_filter_list):
    temp_filter = filter_by_currency(make_long_generator_filter_list, 'USD')
    test_list = []
    for i in range(2):
        test_list.append(next(temp_filter))
    assert test_list == make_generator_filter_list


def test_transaction_base_functions(make_generator_filter_list):
    test_transaction_descriptions = transaction_descriptions(make_generator_filter_list)
    test_list = []
    for i in range(2):
        test_list.append(next(test_transaction_descriptions))
    assert test_list == ["Перевод организации", "Перевод со счета на счет"]


def test_transaction_mistake_iterations(make_generator_filter_list):
    test_transaction_descriptions = transaction_descriptions(make_generator_filter_list)
    with pytest.raises(StopIteration):
        for i in range(12):
            next(test_transaction_descriptions)


@pytest.mark.parametrize('wrong_data',[('13244'),(1231231)])
def test_raises_value_filter_by_currency(wrong_data):
    with pytest.raises(TypeError):
        next(filter_by_currency(wrong_data,'USD'))


@pytest.mark.parametrize('wrong_data',[('13244'),(1231231)])
def test_raises_value_transaction(wrong_data):
    with pytest.raises(TypeError):
        next(transaction_descriptions(wrong_data))


def test_card_number_generator_main_function(card_dannie_info):
    test_card_number = card_number_generator(card_dannie_info[0][0], card_dannie_info[0][1])
    test_list = []
    for i in range (card_dannie_info[0][1]):
        test_list.append(test_card_number)
    assert card_dannie_info[1]


@pytest.mark.parametrize('start, end',[(-10, 10000),(14,10000000000000000000000000)])
def test_card_number_generator_critical_data(start, end):
    with pytest.raises(ValueError):
        card_number_generator(start, end)