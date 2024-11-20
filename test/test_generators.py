import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_generators_filter(make_generator_filter_list):
    temp_filter = filter_by_currency(make_generator_filter_list,'USD')
    test_list = []
    for i in range(2):
        test_list.append(next(temp_filter))
    assert test_list == make_generator_filter_list
