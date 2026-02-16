# This script implements the Modbus network scanning attack, whose objective is to find
# which Unit IDs are active without knowing the network topology. The Modbus TCP uses
# the "Unit ID" to distinguish devices behind a gateway.

from pymodbus.client import ModbusTcpClient
import sys

def scan_network(target_ip, target_port):
    print(f"--- Starting Modbus Network Scanning (Attack B6) on {target_ip}:{target_port} ---")
    
    # tries to connect to the IP address
    client = ModbusTcpClient(target_ip, port=target_port)
    if not client.connect():
        print("It was not possible to connect to the TCP server.")
        return

    # the Modbus has Unit IDs from 1 to 247.
    # an attacker would try all of them, performing a brute-force attack.
    found_units = []
    for unit_id in range(1, 10): 
        try:
            # tries to read a common register. If it responses, it means that the Unit ID exists.
            rr = client.read_holding_registers(address=0, count=1, device_id=unit_id)
            if not rr.isError():
                print(f"[!] ALERT: Device found on the Unit ID: {unit_id}")
                found_units.append(unit_id)
            else:
                # If the server sent an error or timeout it means that there's no Unit ID
                pass
        except Exception as e:
            #pass
            print(f"Erro no ID {unit_id}: {e}")
    
    print(f"--- Scan completed. Number of devices found: {found_units} ---")
    client.close()

if __name__ == "__main__":
    scan_network('localhost', 5020)