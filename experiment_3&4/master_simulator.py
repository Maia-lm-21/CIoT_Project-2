# This script creates the Modbus Master (Client), simulating an operator
# legitimately reading data

from pymodbus.client import ModbusTcpClient
import time

def run_master():
    # connecting to the tcp server - slave
    client = ModbusTcpClient('localhost', port=5020)
    client.connect()
    
    try:
        while True:
            # reads the register number 0
            rr = client.read_holding_registers(address=0, count=1, device_id=1)
            if not rr.isError():
                print(f"[Normal] Sensor reading: {rr.registers[0]}")
            else:
                print("[Error] Failure on reading the sensor!")
            time.sleep(2) # reads every 2 seconds
    except KeyboardInterrupt:
        print("Closing Client...")
        client.close()

if __name__ == "__main__":
    run_master()