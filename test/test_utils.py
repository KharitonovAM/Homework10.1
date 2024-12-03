import pytest
from src.utils import take_data_from_json


def test_with_bad_filename():
    assert take_data_from_json('file_with_bad_name.sfasfasf') == []