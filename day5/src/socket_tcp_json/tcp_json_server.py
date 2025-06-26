# Save this file as tcp_json_server.py

import socket
import json  # For encoding/decoding structured JSON data

# ========================
# --- Server Settings ---
# ========================
HOST = '127.0.0.1'  # Localhost (your machine)
PORT = 65434        # Use a different port than previous examples

# 1. Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))        # Bind to address
server_socket.listen(1)                 # Wait for 1 client
print(f"📡 JSON Server listening on {HOST}:{PORT}...")

# 2. Accept a connection
conn, addr = server_socket.accept()
print(f"🔗 Connection accepted from: {addr}")

# 3. Receive data
data_bytes = conn.recv(1024)
received_json_str = data_bytes.decode('utf-8')  # Convert bytes to string
print(f"📨 Received raw JSON string: {received_json_str}")

# 4. Parse and respond
try:
    received_data_dict = json.loads(received_json_str)  # Parse string to dictionary
    print("✅ Parsed Data:")
    print(f"   Sensor ID : {received_data_dict.get('sensor_id')}")
    print(f"   Value     : {received_data_dict.get('value')}")
    print(f"   Timestamp : {received_data_dict.get('timestamp')}")

    # Respond with confirmation
    response_dict = {"status": "success", "message": "Data received and parsed!"}
    conn.sendall(json.dumps(response_dict).encode('utf-8'))

except json.JSONDecodeError:
    print("❌ Error: Received invalid JSON.")
    error_response = {"status": "error", "message": "Invalid JSON format."}
    conn.sendall(json.dumps(error_response).encode('utf-8'))

# 5. Clean up
conn.close()
server_socket.close()
print("🔚 Server stopped.")