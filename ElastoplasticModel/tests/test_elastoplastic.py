import numpy as np
import pytest
from elastoplastic import isotropic_hardening, kinematic_hardening

# Test input validation
def test_isotropic_hardening_invalid_input():
    with pytest.raises(ValueError):
        isotropic_hardening(0.1, 100, 0.01, -1, 200, 100) 
    with pytest.raises(ValueError):
        isotropic_hardening(0.1, 100, 0.01, 200, -1, 100)  
    with pytest.raises(ValueError):
        isotropic_hardening(0.1, 100, 0.01, 200, 200, -1) 

def test_kinematic_hardening_invalid_input():
    with pytest.raises(ValueError):
        kinematic_hardening(0.1, 100, 0.01, 0, -1, 200, 100)  
    with pytest.raises(ValueError):
        kinematic_hardening(0.1, 100, 0.01, 0, 200, -1, 100)  
    with pytest.raises(ValueError):
        kinematic_hardening(0.1, 100, 0.01, 0, 200, 200, -1)  

# Ｔest isotropic hardening model in elastic state
def test_isotropic_hardening_elastic():
    delta_epsilon = 0.001
    sigma_n = 100
    epsilon_p = 0
    E = 200e3
    Y_0 = 250
    H = 1000

    new_stress, new_epsilon_p = isotropic_hardening(delta_epsilon, sigma_n, epsilon_p, E, Y_0, H)

    assert np.isclose(new_stress, 250.248756, rtol=1e-5, atol=1e-8)
    assert np.isclose(new_epsilon_p, 0.000248756, rtol=1e-5, atol=1e-8)          

# Ｔest isotropic hardening model in plastic state
def test_isotropic_hardening_plastic():
    delta_epsilon = 0.002
    sigma_n = 200
    epsilon_p = 0
    E = 200e3
    Y_0 = 250
    H = 1000

    new_stress, new_epsilon_p = isotropic_hardening(delta_epsilon, sigma_n, epsilon_p, E, Y_0, H)

    assert np.isclose(new_stress, 251.741293, rtol=1e-5, atol=1e-8)
    assert np.isclose(new_epsilon_p, 0.00174129, rtol=1e-5, atol=1e-8)

# Ｔest kinematic hardening model in elastic state
def test_kinematic_hardening_elastic():
    delta_epsilon = 0.001
    sigma_n = 100
    epsilon_p = 0
    alpha_n = 0
    E = 200e3
    Y_0 = 250
    H = 1000

    new_stress, new_epsilon_p, new_alpha_n = kinematic_hardening(delta_epsilon, sigma_n, epsilon_p, alpha_n, E, Y_0, H)

    assert np.isclose(new_stress, 250.248756, rtol=1e-5, atol=1e-8)
    assert np.isclose(new_epsilon_p, 0.000248756, rtol=1e-5, atol=1e-8)
    assert np.isclose(new_alpha_n, 0.248756, rtol=1e-5, atol=1e-8)

# Ｔest kinematic hardening model in plastic state
def test_kinematic_hardening_plastic():
    delta_epsilon = 0.002
    sigma_n = 200
    epsilon_p = 0
    alpha_n = 0
    E = 200e3
    Y_0 = 250
    H = 1000

    new_stress, new_epsilon_p, new_alpha_n = kinematic_hardening(delta_epsilon, sigma_n, epsilon_p, alpha_n, E, Y_0, H)

    assert np.isclose(new_stress, 251.741293, rtol=1e-5, atol=1e-8)
    assert np.isclose(new_epsilon_p, 0.00174129, rtol=1e-5, atol=1e-8)
    assert np.isclose(new_alpha_n, 1.741293, rtol=1e-5, atol=1e-8)
    
# Ｔest negative strain input
def test_negative_strain():
    delta_epsilon = -0.0015
    sigma_n = 100
    epsilon_p = 0
    alpha_n = 0
    E = 200e3 
    Y_0 = 250
    H = 1000
    
    new_stress, new_epsilon_p, new_alpha_n = kinematic_hardening(delta_epsilon, sigma_n, epsilon_p, alpha_n, E, Y_0, H)
    assert np.isclose(new_stress, -200)     
    assert np.isclose(new_epsilon_p, 0)     
    assert np.isclose(new_alpha_n, 0)   
