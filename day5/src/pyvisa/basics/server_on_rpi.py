import socket

HOST = '0.0.0.0'
PORT = 5025

print("🔌 SCPI Server starting on port", PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()
    print(f"✅ Connection accepted from: {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            command = data.decode().strip()
            print(f"📥 Received SCPI command: {command}")

            # --- Send proper response ---
            if command == "*IDN?":
                response = "RPi,SCPI-VISASIM,001,1.0\n"  # Important: newline-terminated
            elif command == "MEAS:TEMP?":
                response = "28.5\n"
            else:
                response = "ERR:UNKNOWN_COMMAND\n"

            # Encode and send response
            conn.sendall(response.encode("utf-8"))
            print(f"📤 Sent: {response.strip()}")