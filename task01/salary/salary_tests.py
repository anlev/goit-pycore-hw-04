from .salary_calculator import calculate_total_and_average_salary
from .salary_parser import parse_salaries
from pathlib import Path

# Tests
def test_calculate_total_and_average_salary_basic():
    total, avg = calculate_total_and_average_salary([3000.0, 2000.0, 1000.0])
    assert total == 6000.0
    assert avg == 2000.0

def test_calculate_total_and_average_salary_empty_returns_zero_average_int():
    total, avg = calculate_total_and_average_salary([])
    assert total == 0.0
    assert avg == 0

def test_calculate_total_and_average_salary_single_value():
    total, avg = calculate_total_and_average_salary([1234.56])
    assert total == 1234.56
    assert avg == 1234.56

base_directory = str(Path(__file__).resolve().parent)

def test_parse_salaries_basic():
    got = parse_salaries(base_directory + "/tests/basic.txt")
    expected = [100.0, 200.0, 300.0]
    assert got == expected, f"TEST failed:\nExpected: {expected}\nGot: {got}"

def test_parse_salaries_empty_file():
    got = parse_salaries(base_directory + "/tests/empty_file.txt")
    expected = []
    assert got == expected, f"TEST failed:\nExpected: {expected}\nGot: {got}"

def test_parse_salaries_no_file():
    got = parse_salaries(base_directory + "/tests/no_file.txt")
    expected = []
    assert got == expected, f"TEST failed:\nExpected: {expected}\nGot: {got}"

def test_parse_salaries_value_errors():
    got = parse_salaries(base_directory + "/tests/value_errors.txt")
    expected = [400.0, 3.0]
    assert got == expected, f"TEST failed:\nExpected: {expected}\nGot: {got}"

def run_salary_tests():
    test_calculate_total_and_average_salary_basic()
    test_calculate_total_and_average_salary_empty_returns_zero_average_int()
    test_calculate_total_and_average_salary_single_value()
    test_parse_salaries_basic()
    test_parse_salaries_empty_file()
    test_parse_salaries_no_file()
    test_parse_salaries_value_errors()