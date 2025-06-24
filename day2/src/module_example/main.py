import sensor_utilities

print(f"PI_VALUE from module: {sensor_utilities.PI_VALUE}")
print(f"298.15 Kelvin in Celsius: {sensor_utilities.kelvin_to_celsius(298.15):.2f}°C")
print(f"Average of [10, 20, 30]: {sensor_utilities.calculate_average([10, 20, 30]):.2f}")
