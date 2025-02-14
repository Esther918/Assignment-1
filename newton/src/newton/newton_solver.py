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
