# Save this code as tcp_simple_client.py

import socket  # Import Python's built-in socket module

# ========================
# --- Client Settings ---
# ========================
HOST = '127.0.0.1'  # IP address of the server (localhost = same machine)
PORT = 65432        # Port number the server is listening on

print("--- TCP Client: Simple Example ---")

# ========================================
# 1. Create a TCP/IP socket
# ========================================
# AF_INET      : Address family for IPv4
# SOCK_STREAM  : Socket type for TCP (reliable stream-based connection)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("✅ Client socket created.")

try:
    # ========================================
    # 2. Connect to the TCP server
    # ========================================
    # Attempts to make a connection to the server at HOST:PORT
    client_socket.connect((HOST, PORT))
    print(f"🔌 Connected to server at {HOST}:{PORT}")

    # ========================================
    # 3. Send data to the server
    # ========================================
    # All data sent over TCP must be bytes, so we encode the string
    message_to_send = "Hello server, this is the client!"
    client_socket.sendall(message_to_send.encode('utf-8'))
    print(f"📤 Client sent: '{message_to_send}'")

    # ========================================
    # 4. Receive a response from the server
    # ========================================
    # Try to receive up to 1024 bytes of response
    data_bytes = client_socket.recv(1024)
    server_response = data_bytes.decode('utf-8')  # Decode from bytes to string
    print(f"📨 Client received: '{server_response}'")

except ConnectionRefusedError:
    print("❗ Connection refused: Is the server running? Check address/port.")
except Exception as e:
    print(f"❗ An unexpected error occurred: {e}")

finally:
    # ========================================
    # 5. Close the client socket
    # ========================================
    client_socket.close()
    print("❌ Client socket closed.")