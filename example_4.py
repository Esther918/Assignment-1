from bisection_solver import bisection_method
# Free fall motion
# The formula of free fall motion: h - 0.5 * g * t^2

g = 9.81
h = 50
f4 = lambda t: h - 0.5 * g * t**2  

root4 = bisection_method(f4, 0, 10, tol=1e-6)  
print(f"It takes {root4} seconds to hit the ground")  # Expected answer: approximate 3.193