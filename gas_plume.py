import numpy as np
import matplotlib.pyplot as plt

# Parameters
Q = 50.0       # Emission rate (g/s)
u = 5.0        # Wind speed (m/s)
H = 10.0       # Stack height (m)

# Distance array (m)
x = np.linspace(10, 1000, 500) 

# Briggs Dispersion Coefficients (Class D - Neutral, Open Country)
# sigma = a * x / (1 + b*x)**c (Simplified version below)
sigma_y = 0.08 * x * (1 + 0.0001 * x)**(-0.5)
sigma_z = 0.06 * x * (1 + 0.0015 * x)**(-0.5)

# Gaussian Plume Equation for ground-level centerline (y=0, z=0)
# Including ground reflection term: 2 * exp(-H^2 / (2 * sigma_z^2))
term1 = Q / (np.pi * u * sigma_y * sigma_z)
term2 = np.exp(-0.5 * (H / sigma_z)**2)
C = term1 * term2 * 1e6  # Convert to µg/m³

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x, C, label=f"Source H={H}m", color='blue', linewidth=2)

plt.title("Ground Level Concentration (Centerline)")
plt.xlabel("Distance Downwind (m)")
plt.ylabel("Concentration (µg/m³)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
