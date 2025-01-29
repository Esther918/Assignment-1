from bisection_solver import bisection_method

f1 = lambda x: x**2 - 4
root1 = bisection_method(f1, 0, 5)
print(f"Root found: {root1}") # Expected root to be approximate 2