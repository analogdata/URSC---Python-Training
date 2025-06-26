import socket

# --- Configuration ---
HOST = '192.168.0.103'   # Replace with your Raspberry Pi's IP address
PORT = 5025              # The port your server is listening on

print("💡 LED Toggle Client Starting...")

# Function to send a command and receive a response
def send_scpi_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"🔌 Connected to {HOST}:{PORT}")

            # Send command
            s.sendall((command + '\n').encode('utf-8'))
            print(f"📤 Sent: {command}")

            # Receive response
            data = s.recv(1024).decode('utf-8').strip()
            print(f"📥 Response: {data}")
            return data

    except ConnectionRefusedError:
        print("❌ Could not connect to server. Is it running?")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# --- Example Usage ---
if __name__ == '__main__':
    # Toggle LED ON
    send_scpi_command("LED ON")

    # Wait a moment (optional)
    import time
    time.sleep(2)

    # Toggle LED OFF
    send_scpi_command("LED OFF")

    # Optionally query the state
    send_scpi_command("LED?")