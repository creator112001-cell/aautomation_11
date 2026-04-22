import pytest
from app import divide

def test_divide_valid():
    """Tests basic division functionality."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(0, 5) == 0

def test_divide_negative_numbers():
    """Tests division involving negative numbers."""
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5

def test_divide_floats():
    """Tests division that results in floating point numbers."""
    assert divide(5, 2) == 2.5
    assert divide(1, 4) == 0.25

def test_divide_by_zero():
    """Ensures that dividing by zero raises the appropriate exception."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)