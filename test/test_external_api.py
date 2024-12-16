from unittest.mock import patch

import pytest

from src.external_api import get_exchange, take_summ_in_ruble


def test_take_summ_in_ruble(database_from_api):
    assert take_summ_in_ruble(database_from_api) == 100000


def test_api_mistake():
    with pytest.raises(TypeError):
        get_exchange(100000)


"""@pytest.mark.parametrize("sum,valuta", [(10000, "aaa")])
def test_with_wrong_data(sum, valuta):
    assert get_exchange(sum, valuta) == {
        "error": {
            "code": "invalid_from_currency",
            "message": 'You have entered an invalid "from" property. [Example: '
            "from=EUR]",
        }
    }"""


@patch("requests.request")
def test_get_exchange(mock_get):
    mock_get.return_value.json.return_value = {
        "info": ["data1", "info2", "info3"],
        "result": 100000,
    }
    assert get_exchange(100, "usd") == {
        "info": ["data1", "info2", "info3"],
        "result": 100000,
    }
