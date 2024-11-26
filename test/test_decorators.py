import pytest
from src.decorators import log


def test_log_decorator():
    @log()
    def add_number(a,b):
        return a+b
    z = add_number(5,7)
    assert 'add_number ok'


def test_log_decorator_with_bad_data():
    @log()
    def divide_number(a,b):
        return a/b
    divide_number(5,0)
    assert 'divide_number error: division by zero. Inputs: (5, 0), {}'

