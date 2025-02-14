import numpy as np
import math

def isotropic_hardening(delta_epsilon, sigma_n, epsilon_p, E, Y_0, H):
    '''
    Variables:
    delta_epsilon = strain increment
    sigma_n = stress
    epsilon_p = plastic strain
    E = Young's modulus
    Y_0 = initial yield stress
    H = hardening modulus 
    '''
    
    # Input validation
    if E <= 0 or Y_0 <= 0 or H < 0:
        raise ValueError("Invalid material properties: E and Y_0 must be positive, H must be non-negative.")
    
    # Compute yield stress
    Y_n = Y_0 + H * epsilon_p
    
    # Elastic trial stress
    trial_stress = sigma_n + E * delta_epsilon

    # Check state
    trial_phi = abs(trial_stress) - Y_n
    
    if trial_phi <= 0:
        # Elastic
        return trial_stress, epsilon_p
    else:
        # Plastic
        delta_epsilon_p = trial_phi / (E + H)
        epsilon_p += delta_epsilon_p * np.sign(trial_stress)
        sigma_n = trial_stress - E * delta_epsilon_p * np.sign(trial_stress)
        return sigma_n, epsilon_p

def kinematic_hardening(delta_epsilon, sigma_n, epsilon_p, alpha_n, E, Y_0, H):
    '''
    Variables:
    delta_epsilon = strain increment
    sigma_n = stress
    epsilon_p = plastic strain
    alpha_n = back stress
    E = Young's modulus
    Y_0 = yield stress
    H = hardening modulus 
    '''
    
    # Input validation
    if E <= 0 or Y_0 <= 0 or H < 0:
        raise ValueError("Invalid material properties: E and Y_0 must be positive, H must be non-negative.")
    
    # Trial state
    trial_stress = sigma_n + E * delta_epsilon
    trial_alpha = alpha_n
    trial_eta = trial_stress - trial_alpha
    trial_phi = abs(trial_eta) - Y_0

    if trial_phi <= 0:
        # Elastic
        return trial_stress, epsilon_p, alpha_n
    else:
        # Plastic
        delta_epsilon_p = trial_phi / (E + H)
        epsilon_p += delta_epsilon_p * np.sign(trial_eta)
        alpha_n += H * delta_epsilon_p * np.sign(trial_eta)
        sigma_n = trial_stress - E * delta_epsilon_p * np.sign(trial_eta)
        return sigma_n, epsilon_p, alpha_n
    
