import pytest
from unittest.mock import patch
from main import main


@patch('main.input', side_effect=['1', 'executed', 'да', 'по возрастанию', "нет", "да", "Перевод"])
def test_main(mock_input):
    main()
