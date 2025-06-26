import socket
import subprocess
import RPi.GPIO as GPIO
import time

# --- GPIO Setup ---
LED_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure LED is OFF initially

# --- Function to Read Temperature ---
def get_rpi_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        temp_str = output.strip().split('=')[1].replace("'C", "")
        return float(temp_str)
    except Exception as e:
        print(f"❌ Error reading temperature: {e}")
        return -1.0

# --- SCPI Socket Server Setup ---
HOST = '0.0.0.0'
PORT = 5025

print(f"🔌 SCPI Server starting on port {PORT}...")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print("🟢 Waiting for SCPI clients...")

        while True:
            conn, addr = server_socket.accept()
            print(f"✅ Connected from: {addr}")

            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            print("🔌 Client disconnected.")
                            break

                        command = data.decode().strip().upper()
                        print(f"📥 Received: {command}")

                        if command == "*IDN?":
                            response = "RPi,SCPI-GPIO,001,1.0\n"
                        elif command == "MEAS:TEMP?":
                            temp = get_rpi_temperature()
                            response = f"{temp:.2f}\n"
                        elif command == "LED ON":
                            GPIO.output(LED_PIN, GPIO.HIGH)
                            print("💡 LED ON")
                            response = "OK:LED_ON\n"
                        elif command == "LED OFF":
                            GPIO.output(LED_PIN, GPIO.LOW)
                            print("💡 LED OFF")
                            response = "OK:LED_OFF\n"
                        else:
                            response = "ERR:UNKNOWN_COMMAND\n"

                        conn.sendall(response.encode("utf-8"))
                        print(f"📤 Sent: {response.strip()}")

                    except ConnectionResetError:
                        print("⚠️ Connection reset by client.")
                        break

except KeyboardInterrupt:
    print("\n🛑 Server stopped by user.")

finally:
    GPIO.cleanup()
    print("🧹 Cleaned up GPIO and shutting down.")