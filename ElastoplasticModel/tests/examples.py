import numpy as np
import matplotlib.pyplot as plt
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

# Example 5: Plot stress strain curve
E = 200e3  
Y_0 = 250  
H = 1000   

strain_increments = np.linspace(0, 0.08, 500)  
stresses_iso = []  
stresses_kin = [] 

# intial value
sigma_n_iso = 0 
epsilon_p_iso = 0 
sigma_n_kin = 0  
epsilon_p_kin = 0  
alpha_n_kin = 0  

for delta_epsilon in strain_increments:
    # Isotropic hardening
    sigma_n_iso, epsilon_p_iso = isotropic_hardening(delta_epsilon, sigma_n_iso, epsilon_p_iso, E, Y_0, H)
    stresses_iso.append(sigma_n_iso)

    # Kinematic hardening
    sigma_n_kin, epsilon_p_kin, alpha_n_kin = kinematic_hardening(delta_epsilon, sigma_n_kin, epsilon_p_kin, alpha_n_kin, E, Y_0, H)
    stresses_kin.append(sigma_n_kin)

# Plot stress strain curve
plt.figure(figsize=(10, 6))
plt.plot(strain_increments, stresses_iso, label="Isotropic Hardening", color="blue")
plt.plot(strain_increments, stresses_kin, label="Kinematic Hardening", color="red", linestyle="--")
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Stress-Strain Curve: Isotropic vs Kinematic Hardening")
plt.legend()
plt.grid(True)
plt.show()
