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
    """Tests division that results in floating point numbers using pytest.approx for precision."""
    assert divide(5, 2) == pytest.approx(2.5)
    assert divide(1, 4) == pytest.approx(0.25)
    assert divide(1, 3) == pytest.approx(1/3)

def test_divide_with_floats():
    """Tests division with floating point inputs."""
    assert divide(10.5, 2) == pytest.approx(5.25)
    assert divide(10, 2.5) == pytest.approx(4.0)
    assert divide(0.1, 0.1) == pytest.approx(1.0)

def test_divide_by_zero():
    """Ensures that dividing by zero (both int and float) raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    with pytest.raises(ZeroDivisionError):
        divide(1, 0.0)
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)

def test_divide_invalid_types():
    """Ensures that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError):
        divide("10", 2)
    with pytest.raises(TypeError):
        divide(10, "2")
    with pytest.raises(TypeError):
        divide(None, 5)


# DevOps Buddy Auto-Fix: Added missing error handling (Mock Fallback)