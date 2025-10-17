import pytest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль запрещено")
        return a / b
    
    def is_prime_number(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 5, 5),
    (100, -50, 50),
])
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (15, 3, 5.0),
    (-10, 2, -5.0),
    (0, 5, 0.0),
])
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Деление на ноль запрещено"):
        calculator.divide(10, 0)

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (1, False),
    (0, False),
    (-5, False),
])
def test_is_prime_number(calculator, n, expected):
    assert calculator.is_prime_number(n) == expected