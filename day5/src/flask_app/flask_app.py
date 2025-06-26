# Save this file as flask_app.py
from flask import Flask, request, jsonify  # Flask essentials

app = Flask(__name__)  # Create the Flask app instance

# --- ROUTES ---

# Root Route: Simple hello message
# Access: http://127.0.0.1:5000/
@app.route('/')
def home():
    return "Hello from Flask API! Try /hello or /echo_name?name=Alice"

# Simple GET route returning JSON
# Access: http://127.0.0.1:5000/hello
@app.route('/hello')
def hello_world():
    return jsonify(message="Hello, Engineers!")

# Route with query parameter (GET)
# Access: http://127.0.0.1:5000/echo_name?name=Alice
@app.route('/echo_name')
def echo_name():
    name = request.args.get('name', 'Guest')
    return jsonify(greeting=f"Hello, {name}!")

# Route for POST request with JSON payload
# Access: http://127.0.0.1:5000/sensor_data
@app.route('/sensor_data', methods=['POST'])
def receive_sensor_data():
    if request.is_json:
        sensor_data = request.json
        sensor_id = sensor_data.get('id', 'N/A')
        value = sensor_data.get('value', 'N/A')
        print(f"Server received sensor data: ID={sensor_id}, Value={value}")
        return jsonify(status="success", received_data=sensor_data), 200
    else:
        return jsonify(status="error", message="Request must be JSON"), 400

# --- RUNNING THE APP ---
if __name__ == '__main__':
    app.run(debug=True)