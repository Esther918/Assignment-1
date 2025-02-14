import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from newton.newton_solver import newton_method
import numpy as np

def test_quadratic():
    # Test quadratic function: f(x) = x^2 - 4
    f1 = lambda x: x**2 - 4
    root1 = newton_method(f1, 1.0, tol=1e-6)
    assert abs(root1 - 2) < 1e-6, "Quadratic test failed"

def test_cubic():
    # Test cubic function: f(x) = x^3 - 8
    f2 = lambda x: x**3 - 8
    root2 = newton_method(f2, 1.5, tol=1e-6)
    assert abs(root2 - 2) < 1e-6, "Cubic test failed"

def test_no_real_root():
    # Test function with no real root: f(x) = x^2 + 1
    f3 = lambda x: x**2 + 1
    try:
        newton_method(f3, 1.0)
        assert False, "No real root test failed (Expected ValueError)"
    except ValueError as e:
        # Check if the error message is correct
        assert "Maximum number of iterations exceeded" in str(e), "Unexpected error message"

def test_too_close_to_zero():
    # Test function with derivative close to zero: f(x) = x^3
    f4 = lambda x: x**3
    try:
        newton_method(f4, 0.0)
        assert False, "Derivative too close to zero test failed (Expected ValueError)"
    except ValueError as e:
        # Check if the error message is correct
        assert "Derivative too close to zero" in str(e), "Unexpected error message"