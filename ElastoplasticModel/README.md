# Elasto-plastic material model
Set up a conda environment:
```bash
conda create --name elastoplastic-model-env python=3.12
```
Activate the environment:
```bash
conda activate elastoplastic-model-env
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
pytest --cov=elastoplastic tests/
```
To run the test:
```bash
pytest -v
```
Run examples:
```bash
python tests/examples.py
```

# Run Examples
**Example 1**
Elastic Loading (Isotropic Hardening)
delta_epsilon = 0.001  
sigma_n = 100          
epsilon_p = 0          
E = 200e3              
Y_0 = 250              
H = 1000
             
Example 1:
New Stress: 250.25 MPa
New Plastic Strain: 0.00025

**Example 2**
Plastic Loading (Isotropic Hardening)
delta_epsilon = 0.002  
sigma_n = 200          
epsilon_p = 0          
E = 200e3              
Y_0 = 250              
H = 1000

Example 2
New Stress: 251.74 MPa
New Plastic Strain: 0.00174

**Example 3**
Elastic Loading (Kinematic Hardening)
delta_epsilon = 0.001  
sigma_n = 100          
epsilon_p = 0         
alpha_n = 0            
E = 200e3             
Y_0 = 250              
H = 1000               

Example 3:
New Stress: 250.25 MPa
New Plastic Strain: 0.00025
New Back Stress: 0.24876 MPa

**Example 4**
Plastic Loading (Kinematic Hardening)
delta_epsilon = 0.002  
sigma_n = 200          
epsilon_p = 0          
alpha_n = 0            
E = 200e3             
Y_0 = 250              
H = 1000               

Example 4:
New Stress: 251.74 MPa
New Plastic Strain: 0.00174
New Back Stress: 1.74129 MPa

**Example 5**
Plot stress strain curve
E = 200e3  
Y_0 = 250  
H = 1000   
