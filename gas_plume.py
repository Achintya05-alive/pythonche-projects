# Gaussian Plume Model - Gas Dispersion Calculator
import numpy as np
import matplotlib.pyplot as plt

print("=== Gas Leak Dispersion Model ===")
Q = float(input("Enter emission rate (g/s): "))
u = float(input("Enter wind speed (m/s): "))
# Dispersion coefficients (Pasquill-Gifford stability class D)
sy = 0.08  # horizontal spread
sz = 0.06  # vertical spread

x = np.linspace(1, 1000, 500)  # distance 1m to 1000m

sigma_y = sy * x
sigma_z = sz * x

# Concentration at ground level (z=0, y=0)
C = (Q / (2 * np.pi * u * sigma_y * sigma_z)) * 1e6  # in micrograms/m3
plt.figure(figsize=(10, 5))
plt.plot(x, C)
plt.xlabel("Distance from source (m)")
plt.ylabel("Concentration (µg/m³)")
plt.title(f"Gas Dispersion Plume\nEmission Rate: {Q} g/s | Wind Speed: {u} m/s")
plt.grid(True)
plt.show()