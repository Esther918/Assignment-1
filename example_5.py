from bisection_solver import bisection_method
# Oscillating spring
# Formula: (k/m)^1/2 = w
import math
m = 2 
k = 50
f5 = lambda omega: omega - math.sqrt(k / m) 
root5 = bisection_method(f5, 0, 10, tol=1e-6) 
print(f"Angular frequency: {root5} rad/s")  # Expected answer: approximate 5