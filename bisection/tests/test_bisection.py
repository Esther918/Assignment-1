from bisection_solver import bisection_method as bisection_method
import pytest

def test_root():
    # Test 1: Root of x^2 - 4 in [0,5] should be ~2
    f1 = lambda x: x**2 - 4
    root1 = bisection_method(f1, 0, 5, tol=1e-6)
    assert abs(root1 - 2) < 1e-6, "Test failed: Root is not approximately 2"

def test_three_roots():
    # Test 2: Root of x^3 - 6x^2 + 11x - 6 in [0, 2.5]
    f = lambda x: x**3 - 6*x**2 + 11*x - 6  # Roots at x=1,2,3
    root = bisection_method(f, 1.5, 2.5, tol=1e-6)
    assert abs(root - 2) < 1e-6, "Test failed: Root is not approximately 2"

def test_no_real_root():
    # Test 3: No root in the interval [-2, 2] for x^2 + 1
    f3 = lambda x: x**2 + 1  # No real root
    with pytest.raises(ValueError, match="Function values at a and b must have opposite signs."):
        bisection_method(f3, -2, 2)

def test_no_interval():
    # Test 4: Invalid interval (a == b)
    f1 = lambda x: x**2 - 4
    with pytest.raises(ValueError, match="Interval bounds 'a' and 'b' must be different."):
        bisection_method(f1, 3, 3)
    
def test_same_sign():
    # Test 5: f(a) and f(b) have same signs
    f1 = lambda x: x**2 - 4
    with pytest.raises(ValueError, match="Function values at a and b must have opposite signs."):
        bisection_method(f1, 3, 5)