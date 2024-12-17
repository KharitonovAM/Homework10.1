import pytest
from unittest.mock import patch
from main import main


@patch(
    "main.input",
    side_effect=["1", "executed", "да", "по возрастанию", "нет", "да", "Перевод"],
)
def test_main(mock_input):
    main()


@patch(
    "main.input",
    side_effect=["1", "таракан", "executed", "да", "по возрастанию", "нет", "нет"],
)
def test_main2(mock_input):
    main()


@patch("main.input", side_effect=["2", "executed", "нет", "нет", "нет"])
def test_main3(mock_input):
    main()
