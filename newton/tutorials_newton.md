Set up a conda environment:
```bash
conda create --name newtons-method-env python=3.12
```
Activate the environment:
```bash
conda activate newtons-method-env
```
Double check that python is version 3.12:
```bash
python --version
```
Ensure that pip is using the most up to date:
```bash
pip install --upgrade pip setuptools wheel
```
Ensure pyproject.toml exists and install the package:
If pyproject.toml is present, run:
```bash
pip install -e .
```
Note: make sure you are in the project root directory and that pyproject.toml exists.
Install pytest and pytest-cov:
(If pytest is not found, install it manually):
```bash
pip install pytest pytest-cov
```
Test that the code is working with pytest:
```bash
PYTHONPATH=. pytest --cov=newton tests/
```
To run the test:
```bash
python tests/test_newton.py
```
# Run examples

**Example 1**

f1 = lambda x: x**2 - 9
root1 = newton_method(f1, 1.0)
print(f"Root: {root1}")  # Expected root to be approximately 3

**Example 2**

f2 = lambda x: np.log(x) - 1
root2 = newton_method(f2, 0.5, tol=1e-6)
print(f"Root: {root2}")  # Expected root to be e (approximately 2.718)

**Example 3**

f3 = lambda x: x**5 - x - 1 
root3 = newton_method(f3, 1.5, tol=1e-6)
print(f"Root: {root3}")  # Expected root to be approximately 1.167

**Example 4**

Free fall motion. Formula: h - 0.5 * g * t^2

g = 9.81
h = 50
f4 = lambda t: h - 0.5 * g * t**2  
root4 = newton_method(f4, 3.0, tol=1e-6)  
print(f"It takes {root4} seconds to hit the ground")  # Expected answer: approximately 3.193

**Example 5**

Oscillating spring. Formula: (k/m)^1/2 = w

m = 2 
k = 50
f5 = lambda omega: omega - math.sqrt(k / m) 
root5 = newton_method(f5, 1.0, tol=1e-6) 
print(f"Angular frequency: {root5} rad/s")  # Expected answer: approximately 5

