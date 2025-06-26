# Save this code as tcp_simple_server.py

import socket  # Import Python's built-in socket module for networking

# ========================
# --- Server Settings ---
# ========================
HOST = '127.0.0.1'  # Loopback address (localhost). Only accessible from the same machine.
PORT = 65432        # Arbitrary non-privileged port (>1023). Avoid ports already in use.

print("--- TCP Server: Simple Example ---")

# ========================================
# 1. Create a TCP/IP socket
# ========================================
# AF_INET      : Address family for IPv4
# SOCK_STREAM  : Socket type for TCP (connection-oriented, reliable)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("✅ Server socket created.")

# ========================================
# 2. Bind the socket to a specific IP and port
# ========================================
# This tells the operating system that this socket will listen on HOST:PORT
server_socket.bind((HOST, PORT))
print(f"✅ Socket bound to {HOST}:{PORT}")

# ========================================
# 3. Start listening for incoming connections
# ========================================
# The argument (1) specifies the max number of queued connections (backlog)
server_socket.listen(1)
print("👂 Server listening for incoming connections...")

# ========================================
# 4. Accept a connection (Blocking call)
# ========================================
# This call blocks until a client connects.
# Returns a new socket `conn` to communicate with the client,
# and `addr` contains the client’s address.
conn, addr = server_socket.accept()
print(f"🔗 Connection accepted from client: {addr}")

# ========================================
# 5. Receive data from the client
# ========================================
# We expect to receive up to 1024 bytes.
# Data is received as bytes, so we decode to string using UTF-8.
data_bytes = conn.recv(1024)
client_message = data_bytes.decode('utf-8')
print(f"📨 Received from client: '{client_message}'")

# ========================================
# 6. Send a response back to the client
# ========================================
# Send a confirmation message.
# We encode the string to bytes before sending.
response = "Hello from server! I got your message."
conn.sendall(response.encode('utf-8'))
print("📤 Response sent to client.")

# ========================================
# 7. Close the client socket
# ========================================
conn.close()
print("❌ Client connection closed.")

# ========================================
# 8. Close the main server socket
# ========================================
server_socket.close()
print("🛑 Server stopped. Socket closed.")