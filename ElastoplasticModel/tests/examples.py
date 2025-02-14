import numpy as np
from elastoplastic import isotropic_hardening, kinematic_hardening

# Example 1: Elastic Loading (Isotropic Hardening)
delta_epsilon = 0.001  
sigma_n = 100          
epsilon_p = 0          
E = 200e3              
Y_0 = 250              
H = 1000               

new_stress, new_epsilon_p = isotropic_hardening(delta_epsilon, sigma_n, epsilon_p, E, Y_0, H)
print("Example 1:")
print(f"New Stress: {new_stress} MPa")
print(f"New Plastic Strain: {new_epsilon_p}")

# Example 2: Plastic Loading (Isotropic Hardening)
delta_epsilon = 0.002  
sigma_n = 200          
epsilon_p = 0          
E = 200e3              
Y_0 = 250              
H = 1000               

new_stress, new_epsilon_p = isotropic_hardening(delta_epsilon, sigma_n, epsilon_p, E, Y_0, H)
print("Example 2:")
print(f"New Stress: {new_stress} MPa")
print(f"New Plastic Strain: {new_epsilon_p}")

# Example 3: Elastic Loading (Kinematic Hardening)
delta_epsilon = 0.001  
sigma_n = 100          
epsilon_p = 0         
alpha_n = 0            
E = 200e3             
Y_0 = 250              
H = 1000               

new_stress, new_epsilon_p, new_alpha_n = kinematic_hardening(delta_epsilon, sigma_n, epsilon_p, alpha_n, E, Y_0, H)

print("Example 3:")
print(f"New Stress: {new_stress} MPa")
print(f"New Plastic Strain: {new_epsilon_p}")
print(f"New Back Stress: {new_alpha_n} MPa")

# Example 4: Plastic Loading (Kinematic Hardening)
delta_epsilon = 0.002  
sigma_n = 200          
epsilon_p = 0          
alpha_n = 0            
E = 200e3             
Y_0 = 250              
H = 1000               

new_stress, new_epsilon_p, new_alpha_n = kinematic_hardening(delta_epsilon, sigma_n, epsilon_p, alpha_n, E, Y_0, H)

print("Example 4:")
print(f"New Stress: {new_stress} MPa")
print(f"New Plastic Strain: {new_epsilon_p}")
print(f"New Back Stress: {new_alpha_n} MPa")

