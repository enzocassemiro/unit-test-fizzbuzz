from fizz_buzz.main import fizz_buzz
import pytest

def test_should_return_number_as_string_when_input_is_one():
    expected = '1'
    assert fizz_buzz(1) == expected

def test_should_return_buzz_when_input_is_five():
    expected = 'Buzz'
    assert fizz_buzz(5) == expected

def test_should_return_fizz_when_input_is_three():
    expected = 'Fizz'
    assert fizz_buzz(3) == expected

def test_should_return_fizzbuzz_when_input_is_multiple_of_three_and_five():
    expected = 'FizzBuzz'
    assert fizz_buzz(15) == expected

def test_should_return_number_as_string_when_input_is_not_multiple_of_3_or_5():
    expected = '7'
    assert fizz_buzz(7) == expected

def test_should_return_number_as_string_when_input_is_zero():
    expected = '0'
    assert fizz_buzz(0) == expected

def test_should_return_fizzbuzz_when_input_is_a_very_large_multiple_of_three_and_five():
    expected = 'FizzBuzz'
    assert fizz_buzz(300000) == expected

def test_should_return_number_as_string_when_input_is_negative():
    expected = '-7'
    assert fizz_buzz(-7) == expected

def test_should_raise_type_error_when_input_is_not_an_integer():
    with pytest.raises(TypeError):
        fizz_buzz('abc')