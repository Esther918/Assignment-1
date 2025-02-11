def newton_method(f, x0: float, tol: float = 1e-6, max_iter: int = 100, h: float = 1e-5) -> float:
    """
    Find a root of the function f using Newton's Method with numerical differentiation.

    Parameters:
    f (function): The function for which the root is sought.
    x0 (float): Initial guess for the root.
    tol (float): The tolerance for stopping condition (default: 1e-6).
    max_iter (int): Maximum number of iterations (default: 100).
    h (float): Step size for numerical differentiation (default: 1e-5).
        Numerical derivatived: f(x)/dx = (f(x+h)-f(x))/h
        
    Returns:
    float: Approximate root of the function.

    Raises:
    ValueError: If the derivative is too close to zero.
    ValueError: If no root is found within max_iter iterations.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = (f(x + h) - f(x)) / h  

        if abs(dfx) < 1e-8:
            raise ValueError("Derivative too close to zero; Newton's method may fail.")

        x_n = x - fx / dfx

        if abs(x_n - x) < tol:
            return x_n

        x = x_n
    raise ValueError("Maximum number of iterations exceeded.")

def check_newton_method():
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

# Run tests
if __name__ == "__main__":
    check_newton_method()
