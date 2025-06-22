def calculate_equivalent_resistance():
    """
    Calculates the equivalent resistance of resistors in series or parallel.
    Handles user input for connection type and validates resistance values.
    """
    print("--- Lab Exercise 1: Resistance Calculation ---")

    while True:
        connection_type = input("Enter connection type (series/parallel): ").strip().lower()
        if connection_type in ["series", "parallel"]:
            break
        else:
            print("Invalid connection type. Please enter 'series' or 'parallel'.")

    resistances = []
    while True:
        num_resistors_str = input("Enter the number of resistors: ")
        try:
            num_resistors = int(num_resistors_str)
            if num_resistors <= 0:
                print("Number of resistors must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the count of resistors.")

    for i in range(num_resistors):
        while True:
            resistor_value_str = input(f"Enter resistance value for resistor {i+1} (Ohms): ")
            try:
                resistor_value = float(resistor_value_str)
                if resistor_value <= 0:
                    print("Resistance value must be positive. Please re-enter.")
                else:
                    resistances.append(resistor_value)
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for resistance.")

    equivalent_resistance = 0.0

    if connection_type == "series":
        equivalent_resistance = sum(resistances)
        print(f"\nResistors in series: {resistances}")
        print(f"Equivalent Resistance (Series): {equivalent_resistance:.2f} Ohms")
    elif connection_type == "parallel":
        # Handle the case where there are no resistors to avoid division by zero
        if not resistances:
            print("No resistors provided for parallel calculation.")
            return

        sum_of_reciprocals = 0.0
        for r in resistances:
            # Ensure no division by zero for individual resistors in parallel
            if r == 0:
                print("Warning: Encountered a 0 Ohm resistor in parallel. Equivalent resistance is 0.")
                equivalent_resistance = 0.0
                break # Short-circuit if one resistor is 0 in parallel
            sum_of_reciprocals += (1 / r)
        else: # This else block executes if the for loop completes without a break
            if sum_of_reciprocals == 0:
                # This case implies all resistances were infinite or invalid, which should have been caught
                # by validation. But as a safeguard:
                print("Error: Sum of reciprocals is zero. Cannot calculate parallel resistance.")
            else:
                equivalent_resistance = 1 / sum_of_reciprocals
                print(f"\nResistors in parallel: {resistances}")
                print(f"Equivalent Resistance (Parallel): {equivalent_resistance:.2f} Ohms")

# Uncomment the line below to run Lab Exercise 1
calculate_equivalent_resistance()