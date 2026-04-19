import pytest
from src.decorators import log


# Тест успешного выполнения (вывод в консоль)
def test_log_console_success(capsys):
    @log()
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


# Тест ошибки (вывод в консоль)
def test_log_console_error(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


# Тест успешного выполнения (запись в файл)
def test_log_file_success(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    multiply(3, 4)

    assert log_file.read_text().strip() == "multiply ok"


# Тест ошибки (запись в файл)
def test_log_file_error(tmp_path):
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def get_element(lst, index):
        return lst[index]

    with pytest.raises(IndexError):
        get_element([1, 2], 5)

    content = log_file.read_text().strip()
    assert "get_element error: IndexError. Inputs: ([1, 2], 5), {}" in content


# Тест работы с именованными аргументами (kwargs)
def test_log_with_kwargs(capsys):
    @log()
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}"

    greet("Anna", greeting="Hi")
    captured = capsys.readouterr()
    assert "greet ok" in captured.out
