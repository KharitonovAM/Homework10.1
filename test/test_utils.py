import pytest
from src.utils import take_data_from_json
import os
import json


def test_with_bad_filename():
    assert take_data_from_json('file_with_bad_name.sfasfasf') == []

@pytest.mark.parametrize( "filename, rezult", [('test.json',[]), ('asfasfasdf.json',[])])
def test_empy_file(filename,rezult):
    temp_file = open(filename,'a', encoding='utf-8')
    temp_file.write('""')
    temp_file.close()
    my_result = take_data_from_json(filename)
    os.remove(filename)
    assert my_result == rezult

def test_empty_file_2():
    temp_file = open('test.json', 'a', encoding='utf-8')
    temp_file.write('" "')
    temp_file.close()
    z = take_data_from_json('test.json')
    os.remove('test.json')
    assert z == []

def test_not_list_result(string_data):
    assert take_data_from_json(string_data[0]) == []