# Save this file as tcp_json_client.py

import socket
import json  # For structured data format

# ========================
# --- Client Settings ---
# ========================
HOST = '127.0.0.1'  # Server IP (same as server)
PORT = 65434        # Same port as server

# 1. Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 2. Connect to the server
    client_socket.connect((HOST, PORT))
    print(f"✅ Connected to JSON server at {HOST}:{PORT}")

    # 3. Prepare structured sensor data
    sensor_data = {
        "sensor_id": "TEMP_001",
        "value": 28.5,
        "unit": "Celsius",
        "timestamp": "2025-07-01T14:30:00"
    }

    # Convert to JSON string and send
    json_message_str = json.dumps(sensor_data)
    client_socket.sendall(json_message_str.encode('utf-8'))
    print(f"📤 Client sent structured data: {json_message_str}")

    # 4. Receive and decode response
    response_bytes = client_socket.recv(1024)
    response_json_str = response_bytes.decode('utf-8')
    response_dict = json.loads(response_json_str)
    print(f"📥 Client received structured response: {response_dict}")

except ConnectionRefusedError:
    print("❗ Connection refused: Is the JSON server running?")
except Exception as e:
    print(f"❗ Unexpected error: {e}")
finally:
    client_socket.close()
    print("❌ Client socket closed.")