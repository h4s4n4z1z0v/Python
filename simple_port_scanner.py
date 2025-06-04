import socket  # for making network connections
from concurrent.futures import ThreadPoolExecutor  # for faster scanning using threads

# Function to scan a single port on a given IP
def scan_port(ip, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # set timeout for connection attempt (1 second)
        result = sock.connect_ex((ip, port))  # attempt to connect
        sock.close()  # close the socket
        # If connect_ex returns 0, the port is open
        return port if result == 0 else None
    except:
        # In case of any error (e.g., invalid IP), return None
        return None

# Function to scan a range of ports on a given IP
def port_scanner(ip, start_port=1, end_port=1024):
    open_ports = []  # list to store open ports
    # Use ThreadPoolExecutor to scan multiple ports in parallel (100 threads)
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Submit all scan_port jobs to the executor
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        # As futures complete, check if the port is open
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)  # add open port to the list
    return open_ports  # return the list of open ports

if __name__ == "__main__":
    # Prompt user to enter target IP address
    target_ip = input("Enter target IP address: ").strip()
    print(f"Scanning {target_ip} for open ports from 1 to 1024...")
    # Run the port scanner and get open ports
    open_ports = port_scanner(target_ip)
    # Print the list of open ports
    print(f"Open ports: {open_ports}")
