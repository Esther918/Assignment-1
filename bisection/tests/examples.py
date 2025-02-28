from bisection_solver import bisection_method as bisection_method
import math

# Example 1
f1 = lambda x: x**2 - 4
root1 = bisection_method(f1, 0, 5)
print("Example 1:")
print(f"Root: {root1}") # Expected root to be approximate 2

# Example 2
import math
f2 = lambda x: math.exp(x) - 3*x 
root2 = bisection_method(f2, 0, 1, tol=1e-6)
print("Example 2:")
print(f"Root: {root2}")  # Expected root to be approximate 0.619

# Example 3
f3 = lambda x: x**5 - x - 1 
root3 = bisection_method(f3, 1, 2, tol=1e-6)
print("Example 3:")
print(f"Root: {root3}")  # Expected root to be approximate 1.167

# Example 4
# Free fall motion. Formula: h - 0.5 * g * t^2
g = 9.81
h = 50
f4 = lambda t: h - 0.5 * g * t**2  
root4 = bisection_method(f4, 0, 10, tol=1e-6)  
print("Example 4:")
print(f"It takes {root4} seconds to hit the ground")  # Expected answer: approximate 3.193

# Example 5
# Oscillating spring. Formula: (k/m)^1/2 = w
m = 2 
k = 50
f5 = lambda omega: omega - math.sqrt(k / m) 
root5 = bisection_method(f5, 0, 10, tol=1e-6) 
print("Example 5:")
print(f"Angular frequency: {root5} rad/s")  # Expected answer: approximate 5
