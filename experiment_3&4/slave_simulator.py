# This script creates the Modbus Slave (server), simulating a sensor

from pymodbus.server import StartTcpServer
import logging
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusDeviceContext

# logs to see what is happening in our Modbus 
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_server():
    # simulates 100 registers (Holding Registers) starting in 0 and sets their values to 0.
    block = ModbusSequentialDataBlock(0, [0]*100)
    store = ModbusDeviceContext(hr=block)
    context = ModbusServerContext(devices=store, single=True)

    print("--- Modbus Server Simulator (Slave) running on port 5020 ---")
    print("--- Waiting for connections... ---")
    
    # starts the TCP server on port 5020 (so it doesn't need sudo permissions)
    StartTcpServer(context=context, address=("localhost", 5020))

if __name__ == "__main__":
    run_server()