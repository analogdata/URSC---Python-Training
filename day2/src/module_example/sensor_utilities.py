def kelvin_to_celsius(k):
    return k - 273.15

def calculate_average(readings):
    if not readings:
        return 0.0
    return sum(readings) / len(readings)

PI_VALUE = 3.14159
