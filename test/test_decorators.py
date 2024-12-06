from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log_decorator() -> None:
    @log()
    def add_number(a, b):
        return a + b

    add_number(5, 7)
    assert "add_number ok"


def test_log_decorator_with_bad_data() -> None:
    @log()
    def divide_number(a, b):
        return a / b

    divide_number(5, 0)
    assert "divide_number error: division by zero. Inputs: (5, 0), {}"


def test_capsys_log_decorator(capsys: CaptureFixture[str]) -> None:
    @log()
    def minus_number(a, b, c, d):
        result = a - b - c - d
        print(result)
        return result

    minus_number(100, 50, 30, 20)
    captured = capsys.readouterr()
    assert captured.out == "0\nminus_number ok\n"


def test_capsys_error_decorator(capsys: CaptureFixture[str]) -> None:
    @log()
    def add_number(a, b, c):
        return a + b + c

    add_number(3, 4, "u")
    capture = capsys.readouterr()
    assert (
        capture.out
        == """add_number error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (3, 4, 'u'), {}\n"""
    )


def test_write_to_file():
    @log("data/test_log.txt")
    def mytest_add_number(a, b):
        return a + b

    mytest_add_number(5, 8)
    with open("data/test_log.txt", "r") as f:
        test_data = f.readlines()
    assert test_data[-1] == "mytest_add_number ok\n"


def test_write_error_to_file():
    @log("data/test_log.txt")
    def mytest_add_number(a, b):
        return a + b

    mytest_add_number(5, ["123", "123"])
    with open("data/test_log.txt", "r") as f:
        test_data = f.readlines()
    assert (
        test_data[-1]
        == """mytest_add_number error: unsupported operand type(s) for +: 'int' and 'list'. Inputs: (5, ['123', '123']), {}\n"""
    )
