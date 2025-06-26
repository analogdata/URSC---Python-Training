# flask_form_app.py
# ---------------------------------------------
# This is a basic Flask web app that allows users to submit sensor data (ID, Temperature, Pressure)
# using a form built with Tailwind CSS. The data is processed and shown back on the same page.
# ---------------------------------------------

from flask import Flask, request, render_template_string

# Create a Flask web application instance
app = Flask(__name__)

# ---------------------------------------------
# HTML FORM as a string (usually you'd keep this in a separate .html file inside the "templates" folder)
# We're embedding it here for simplicity in a single-file app.
# ---------------------------------------------
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Process Sensor Data</title>
    <!-- Tailwind CSS for styling -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <!-- Google Outfit font -->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500&display=swap" rel="stylesheet">
    <style>
        html, body {
            font-family: 'Outfit', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-sm">
        <h2 class="text-2xl font-bold mb-6 text-gray-800 text-center">Sensor Data Input (Flask)</h2>

        <!-- Form submission to /process_sensor_form route -->
        <form action="/process_sensor_form" method="POST">
            <!-- Sensor ID Field -->
            <div class="mb-4">
                <label for="sensor_id" class="block text-gray-700 text-sm font-bold mb-2">Sensor ID:</label>
                <input type="text" id="sensor_id" name="sensor_id" class="input-field shadow appearance-none border rounded w-full py-2 px-3 text-gray-700" required>
            </div>

            <!-- Temperature Field -->
            <div class="mb-4">
                <label for="temperature" class="block text-gray-700 text-sm font-bold mb-2">Temperature (°C):</label>
                <input type="number" step="0.1" id="temperature" name="temperature" class="input-field shadow appearance-none border rounded w-full py-2 px-3 text-gray-700" required>
            </div>

            <!-- Pressure Field (Optional) -->
            <div class="mb-6">
                <label for="pressure" class="block text-gray-700 text-sm font-bold mb-2">Pressure (kPa):</label>
                <input type="number" step="0.1" id="pressure" name="pressure" class="input-field shadow appearance-none border rounded w-full py-2 px-3 text-gray-700">
            </div>

            <!-- Submit Button -->
            <div class="flex items-center justify-between">
                <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-full">
                    Submit Data
                </button>
            </div>
        </form>

        <!-- Section to display result if available -->
        {% if result %}
        <div class="mt-6 p-4 bg-green-100 border border-green-400 text-green-700 rounded relative">
            <strong class="font-bold">Success!</strong>
            <span class="block sm:inline">Data Received: {{ result }}</span>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

# ---------------------------------------------
# Route: Show the form to the user
# ---------------------------------------------
@app.route('/')
def show_input_form():
    return render_template_string(HTML_FORM, result=None)

# ---------------------------------------------
# Route: Process the submitted form data (POST)
# ---------------------------------------------
@app.route('/process_sensor_form', methods=['POST'])
def process_sensor_form():
    # Extract values from form submission
    sensor_id = request.form['sensor_id']
    temperature = request.form['temperature']
    pressure = request.form.get('pressure', 'N/A')  # Optional: default to 'N/A' if not provided

    try:
        # Convert temperature and pressure to float (if provided)
        temp_float = float(temperature)
        pressure_float = float(pressure) if pressure != 'N/A' else None

        # Format the result message
        processed_message = f"Sensor ID: {sensor_id}, Temp: {temp_float}°C, Pressure: {pressure_float if pressure_float is not None else 'N/A'} kPa"

        # Print to console (simulating saving to DB or further processing)
        print(f"Server received and processed: {processed_message}")

        # Render the same form again, but show result
        return render_template_string(HTML_FORM, result=processed_message)

    except ValueError:
        # Handle case where input is not a number
        return render_template_string(HTML_FORM, result="Error: Temperature and Pressure must be valid numbers.")

# ---------------------------------------------
# Start the Flask app on port 5001
# ---------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5001)