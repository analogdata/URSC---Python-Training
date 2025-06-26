import struct
import json

print("\n--- Protocol Design: Binary vs. JSON ---")

# ---------------------------
# JSON Example (Human-readable)
# ---------------------------
# This is how data is usually exchanged on the web – readable but slightly heavy.

json_data = {
    "id": "S1",       # String ID (2 characters)
    "val": 25.5       # Temperature value
}

# Convert the dictionary into a UTF-8 encoded byte string
json_bytes = json.dumps(json_data).encode('utf-8')

print(f"📝 JSON Data: {json_data}")
print(f"📦 JSON Bytes: {json_bytes} (Length: {len(json_bytes)} bytes)")

# ---------------------------
# Binary Protocol Example (Compact, not human-readable)
# ---------------------------
# Use struct to pack raw numbers efficiently into bytes.

sensor_id_bin = 101        # Integer (short)
temperature_bin = 28.75    # Float

# Struct format: '<h f' means:
# <  : Little-endian (byte order)
# h  : Short integer (2 bytes)
# f  : Float (4 bytes)
binary_packet = struct.pack('<h f', sensor_id_bin, temperature_bin)

print(f"\n🔧 Binary Data: Sensor ID = {sensor_id_bin}, Temperature = {temperature_bin}")
print(f"📦 Binary Bytes: {binary_packet} (Length: {len(binary_packet)} bytes)")

# Unpack the bytes back to Python values
unpacked_id, unpacked_temp = struct.unpack('<h f', binary_packet)

print(f"🔓 Unpacked Binary: ID = {unpacked_id}, Temp = {unpacked_temp}")

# ---------------------------
# Size Comparison
# ---------------------------
print("\n📏 Comparing data sizes:")
print(f"JSON Payload Length  : {len(json_bytes)} bytes")
print(f"Binary Payload Length: {len(binary_packet)} bytes")