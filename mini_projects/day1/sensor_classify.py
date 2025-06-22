def classify_sensor_reading():
    """
    Classifies a sensor reading into 'Safe', 'Warning', 'Critical', or 'Invalid/Error'
    based on predefined ranges.
    """
    print("\n--- Lab Exercise 2: Sensor Reading Classification ---")

    # Define thresholds as constants for easy modification
    MIN_VALID_READING = 0.0
    MAX_VALID_READING = 1000.0 # This reading itself is considered invalid/error, bounds are exclusive
    SAFE_THRESHOLD_HIGH = 100.0 # < 100 is Safe
    WARNING_THRESHOLD_HIGH = 500.0 # < 500 is Warning (100 to 499.99)
    # CRITICAL_THRESHOLD_HIGH implicitly starts from 500 up to <1000

    while True:
        reading_str = input("Enter sensor reading (numeric, or 'quit' to exit): ").strip().lower()
        if reading_str == 'quit':
            print("Exiting sensor classification.")
            break

        try:
            reading = float(reading_str)

            classification = ""
            alert_message = ""

            # Check for invalid/error range first (most extreme conditions)
            if reading < MIN_VALID_READING or reading >= MAX_VALID_READING:
                classification = "Invalid/Error"
                alert_message = "Reading outside expected operating range! Sensor malfunction suspected."
            elif reading >= WARNING_THRESHOLD_HIGH: # Covers 500 up to <1000
                classification = "Critical"
                alert_message = "Immediate action required!"
            elif reading >= SAFE_THRESHOLD_HIGH: # Covers 100 up to <500
                classification = "Warning"
                alert_message = "Needs attention, but not critical."
            else: # Covers 0 up to <100
                classification = "Safe"
                alert_message = "Within the safe operating zone."

            print(f"Sensor Reading: {reading:.2f}")
            print(f"Classification: {classification}")
            print(f"Alert: {alert_message}\n")

        except ValueError:
            print("Invalid input. Please enter a numerical value for the reading or 'quit'.\n")


# Uncomment the line below to run Lab Exercise 2
classify_sensor_reading()