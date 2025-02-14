from newton import newton_method
import numpy as np
import math

def test_newton_method():
    # Test 1: Quadratic
    f1 = lambda x: x**2 - 4
    root1 = newton_method(f1, 1.0, tol=1e-6)
    assert abs(root1 - 2) < 1e-6, "Test 1 failed"
    print("Test 1 passed")

    # Test 2: Cubic
    f2 = lambda x: x**3 - 8
    root2 = newton_method(f2, 1.5, tol=1e-6)
    assert abs(root2 - 2) < 1e-6, "Test 2 failed"
    print("Test 2 passed")

    # Test 3: No real root for x^2 + 1
    f3 = lambda x: x**2 + 1
    try:
        newton_method(f3, 1.0)
        assert False, "Test 3 failed (Expected ValueError)"
    except ValueError:
        print("Test 3 passed")

    # Test 4: Derivative too close to zero
    f4 = lambda x: x**3
    try:
        newton_method(f4, 0.0)
        assert False, "Test 4 failed (Expected ValueError)"
    except ValueError:
        print("Test 4 passed")

    print("All tests passed")

