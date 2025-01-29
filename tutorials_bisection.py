def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Find a root of the function f using the Bisection Method.
    Here's how it works. Choose an interval [a,b] where there's at least one root in the interval, 
    which means f(a) and f(b) have opposite signs. Repeatedly halving the interval to approximate the root 
    until it is found within a tolerance.

    Parameters:
    f: Function
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    tol (float): The tolerance for stopping condition.
    max_iter (int): Maximum number of iterations.

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
        c = (a + b) / 2 
        fc = f(c)

        if abs(fc) < tol:
            return c
        
        # Narrow the interval
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    raise ValueError("Root not found within the maximum number of iterations.")

# Examples of using solver

# Example 1
f1 = lambda x: x**2 - 4
root1 = bisection_method(f1, 0, 5)
print(f"Root: {root1}") # Expected root to be approximate 2

# Example 2
import math
f2 = lambda x: math.exp(x) - 3*x 
root2 = bisection_method(f2, 0, 1, tol=1e-6)
print(f"Root: {root2}")  # Expected root to be approximate 0.619

# Example 3
f3 = lambda x: x**5 - x - 1 
root3 = bisection_method(f3, 1, 2, tol=1e-6)
print(f"Root: {root3}")  # Expected root to be approximate 1.167

# Example 4
# Free fall motion. Formula: h - 0.5 * g * t^2
g = 9.81
h = 50
f4 = lambda t: h - 0.5 * g * t**2  
root4 = bisection_method(f4, 0, 10, tol=1e-6)  
print(f"It takes {root4} seconds to hit the ground")  # Expected answer: approximate 3.193

# Example 5
# Oscillating spring. Formula: (k/m)^1/2 = w
m = 2 
k = 50
f5 = lambda omega: omega - math.sqrt(k / m) 
root5 = bisection_method(f5, 0, 10, tol=1e-6) 
print(f"Angular frequency: {root5} rad/s")  # Expected answer: approximate 5
