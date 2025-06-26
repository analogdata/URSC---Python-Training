import socket
import subprocess

HOST = '0.0.0.0'
PORT = 5025

def get_rpi_temperature():
    """Fetch CPU temperature from Raspberry Pi using vcgencmd."""
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        # Output format: temp=48.9'C
        temp_str = output.strip().split('=')[1].replace("'C", "")
        return float(temp_str)
    except Exception as e:
        print(f"Error getting temperature: {e}")
        return -1.0

print(f"🔌 SCPI Temperature Server starting on port {PORT}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print("🟢 Waiting for SCPI client connection...")

    conn, addr = s.accept()
    print(f"✅ Connection accepted from: {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            command = data.decode().strip()
            print(f"📥 Received SCPI command: {command}")

            if command == "*IDN?":
                response = "RPi,SCPI-TEMP,001,1.0\n"
            elif command == "MEAS:TEMP?":
                temp = get_rpi_temperature()
                response = f"{temp:.2f}\n"
            else:
                response = "ERR:UNKNOWN_COMMAND\n"

            conn.sendall(response.encode('utf-8'))
            print(f"📤 Sent: {response.strip()}")