def error_code_lookup():
    """
    Provides a system to look up error codes and their descriptions from a dictionary.
    Allows continuous lookups until the user quits.
    """
    print("\n--- Lab Exercise 3: Error Code Lookup ---")

    # Error code dictionary: Key (int) -> Value (dict with description and action)
    error_data = {
        101: {"description": "Sensor calibration required.", "action": "Run diagnostic on affected sensor."},
        102: {"description": "Telemetry link intermittent.", "action": "Check antenna alignment and signal strength."},
        205: {"description": "Power supply unit low voltage.", "action": "Inspect power input, replace PSU if necessary."},
        310: {"description": "Actuator response delayed.", "action": "Check hydraulic fluid levels and actuator motor."},
        404: {"description": "Software module not found.", "action": "Verify module installation and path configuration."},
        500: {"description": "Critical system overload.", "action": "Immediate system shutdown and power cycle. Analyze logs."}
    }

    print("Available Error Codes (for reference):")
    # Print sorted keys for easy reference during the lab
    print(sorted(error_data.keys()))
    print("Type 'quit' to exit lookup.")

    while True:
        code_input = input("Enter error code to lookup: ").strip().lower()

        if code_input == 'quit':
            print("Exiting error code lookup.")
            break

        try:
            error_code = int(code_input)
            
            # Use dict.get() for safe lookup, providing a default message if not found
            info = error_data.get(error_code)

            if info:
                print(f"\n--- Details for Error Code {error_code} ---")
                print(f"Description: {info['description']}")
                print(f"Recommended Action: {info['action']}")
                print("-------------------------------------------\n")
            else:
                print(f"Error code '{error_code}' not found in the database. Please check the code.\n")

        except ValueError:
            print("Invalid input. Please enter a numerical error code or 'quit'.\n")

# Uncomment the line below to run Lab Exercise 3
error_code_lookup()
