import pyvisa

rm = pyvisa.ResourceManager('@py')  # Force using PyVISA-py backend

# Open the socket resource
inst = rm.open_resource("TCPIP0::192.168.0.103::5025::SOCKET")

# ✅ Set termination settings
inst.read_termination = '\n'
inst.write_termination = '\n'
inst.timeout = 3000  # in milliseconds (3 seconds, adjust if needed)

# Now query
print(inst.query("*IDN?"))       # Should print: RPi,SCPI-VISASIM,001,1.0
print(inst.query("MEAS:TEMP?"))  # Should print: 28.5