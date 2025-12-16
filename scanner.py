import socket
from concurrent.futures import ThreadPoolExecutor
import time

# ----------------------------------------
# Get target input from the user
# ----------------------------------------
# Target IP address or domain name to scan
# (Scan only systems you own or have permission for)
target = input("Enter target IP or domain: ")

# Common ports to scan
ports = [21, 22, 80, 443, 3306]

# List to store open ports
open_ports = []

def scan_port(port):
    """
    Scans a single TCP port on the target host.
    This function is executed by multiple threads.
    """
    try:
        # Create a TCP socket using IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout to avoid hanging on filtered ports
        s.settimeout(1)

        # Attempt to connect to the target and port
        # connect_ex() returns 0 if the port is open
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is Open")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is Closed")

    except socket.error as e:
        # Handle socket-related errors gracefully
        print(f"Error connecting to port {port}: {e}")

    finally:
        # Always close the socket to free system resources
        s.close()

# ----------------------------------------
# Scan start
# ----------------------------------------
print("\n[+] Scan starting...")
start_time = time.time()

try:
    # Create a thread pool for faster scanning
    # max_workers controls how many threads run concurrently
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Assign each port to the scan_port function
        executor.map(scan_port, ports)

except KeyboardInterrupt:
    # Allows the user to stop the scan using Ctrl + C
    print("\n[!] Scan interrupted by user")

# ----------------------------------------
# Scan end
# ----------------------------------------
end_time = time.time()
total_time = end_time - start_time

print("\n[+] Scan completed")
print(f"[+] Start Time : {time.ctime(start_time)}")
print(f"[+] End Time   : {time.ctime(end_time)}")
print(f"[+] Total Time : {total_time:.2f} seconds")

# Display open ports found during the scan
print("\n[+] Open Ports Found:")
for p in open_ports:
    print(f"    - {p}")
