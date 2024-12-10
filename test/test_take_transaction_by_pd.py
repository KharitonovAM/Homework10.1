import pytest
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