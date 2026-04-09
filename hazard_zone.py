# Explosive Hazard Zone Calculator
# Based on TNT Hopkinson-Cranz Scaling Law

print("=== Explosive Hazard Zone Calculator ===")
weight = float(input("Enter explosive weight in kg: "))
fatality_zone = 5 * (weight ** (1/3))
injury_zone = 14 * (weight ** (1/3))
print(f"\nFor {weight} kg of explosive:")
print(f"Fatality Zone: {fatality_zone:.2f} metres")
print(f"Injury Zone  : {injury_zone:.2f} metres")