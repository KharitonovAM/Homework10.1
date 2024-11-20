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