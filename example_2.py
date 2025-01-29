from bisection_solver import bisection_method
import math
f2 = lambda x: math.exp(x) - 3*x 
root2 = bisection_method(f2, 0, 1, tol=1e-6)
print(f"Root found: {root2}")  # Expected root to be approximate 0.619