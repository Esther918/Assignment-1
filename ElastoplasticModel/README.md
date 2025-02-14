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
