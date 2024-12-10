import pytest
import pandas as pd
import os
from unittest.mock import Mock, patch
from src.take_transaction_by_pb import take_transactions_from_exel, take_transactions_from_csv


@patch('csv.DictReader', return_value = [{'data':'123', 'name':'MyName'}, {'data':121, 'name':'Alice'}])
def test_take_transactions_from_csv(mock_csv_DictReader):
    open('test.csv','w')
    assert take_transactions_from_csv('test.csv') == [{'data':'123', 'name':'MyName'}, {'data':121, 'name':'Alice'}]
    mock_csv_DictReader.assert_called_once()
    os.remove('test.csv')


def test_with_wrong_file_csv():
    with pytest.raises(FileNotFoundError):
        raise take_transactions_from_csv('bad filename')


def test_with_wrong_file_exel():
    with pytest.raises(FileNotFoundError):
        raise take_transactions_from_exel('bad filename')



def test_patch_test_take_transactions_from_exel():
    z = [{'name': 'Ivan', 'family': 'Бунин'}, {'name': 'Olga', 'family': 'Кортункова'}]
    my_datafraim = pd.DataFrame(z)
    my_datafraim.to_excel('my_exel.xlsx', index=False)
    assert take_transactions_from_exel('my_exel.xlsx') == [{'name': 'Ivan', 'family': 'Бунин'}, {'name': 'Olga', 'family': 'Кортункова'}]
    os.remove('my_exel.xlsx')