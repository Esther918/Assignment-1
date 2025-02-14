# Bisection's Method
Set up a conda environment:
```bash
conda create --name bisection-method-env python=3.12
```
Activate the environment:
```bash
conda activate bisection-method-env
```
Double check that python is version 3.12:
```bash
python --version
```
Ensure that pip is using the most up to date:
```bash
pip install --upgrade pip setuptools wheel
```
```bash
python -m pip install --upgrade pip
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
pytest --cov=bisection_solver tests/
```
To run the test:
```bash
pytest -v
```
Run examples:
```bash
python tests/examples.py
```
# Run examples

**Example 1**

f1 = lambda x: x**2 - 4
root1 = bisection_method(f1, 0, 5)
Expected root to be approximate 2

**Example 2**

f2 = lambda x: math.exp(x) - 3*x 
root2 = bisection_method(f2, 0, 1, tol=1e-6)
Expected root to be approximate 0.619

**Example 3**

f3 = lambda x: x**5 - x - 1 
root3 = bisection_method(f3, 1, 2, tol=1e-6)
Expected root to be approximate 1.167

**Example 4**

Free fall motion. Formula: h - 0.5 * g * t^2
g = 9.81
h = 50
f4 = lambda t: h - 0.5 * g * t**2  
root4 = bisection_method(f4, 0, 10, tol=1e-6)  
It takes 3.193 seconds to hit the ground

**Example 5**

Oscillating spring. Formula: (k/m)^1/2 = w
m = 2 
k = 50
f5 = lambda omega: omega - math.sqrt(k / m) 
root5 = bisection_method(f5, 0, 10, tol=1e-6) 
Angular frequency: 5 rad/s
