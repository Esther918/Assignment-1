def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Find a root of the function f using the Bisection Method.

    Parameters:
    f (function): The function for which the root is sought.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    tol (float): The tolerance for stopping condition (default: 1e-6).
    max_iter (int): Maximum number of iterations (default: 100).

    Returns:
    float: Approximate root of the function.

    Raises:
    ValueError: If f(a) and f(b) do not have opposite signs.
    ValueError: If a and b are the same.
    ValueError: If no root is found within max_iter iterations.
    """

    # Validate input
    if a == b:
        raise ValueError("Interval bounds 'a' and 'b' must be different.")
    
    fa, fb = f(a), f(b)
    
    if fa * fb > 0:
        raise ValueError("Function values at a and b must have opposite signs.")

    # Bisection method iterations
    for _ in range(max_iter):
        c = (a + b) / 2  # Midpoint
        fc = f(c)

        if abs(fc) < tol:  # Convergence check
            return c
        
        # Narrow the interval
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    raise ValueError("Root not found within the maximum number of iterations.")

