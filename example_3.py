from bisection_solver import bisection_method

f3 = lambda x: x**5 - x - 1 
root3 = bisection_method(f3, 1, 2, tol=1e-6)
print(f"Root found: {root3}")  # Expected root to be approximate 1.167