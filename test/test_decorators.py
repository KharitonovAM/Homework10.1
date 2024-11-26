import pytest
from src.decorators import log



def test_log_decorator():
    @log()
    def add_number(a,b):
        return a+b
    assert 'add_number ok'
