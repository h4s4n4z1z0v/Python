import socket

# Define ports and their typical services
ports_services = {
    21: 'FTP',
    53: 'DNS',
    80: 'HTTP',
    194: 'IRC',
}

# Function to scan a single port and try to get a banner if possible
def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout so it doesn't hang forever
        sock.settimeout(1)
        # Try to connect to the port
        result = sock.connect_ex((ip, port))
        if result == 0:
            # If open, send a simple request (for HTTP-style banners)
            sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            # Receive response
            banner = sock.recv(1024).decode('utf-8', errors='ignore')
            return True, banner.strip()
        sock.close()
    except Exception:
        pass
    return False, ''

# Main scanning function
def main():
    # Get the target IP address from the user
    target_ip = input("Enter target IP: ")
    print(f"Scanning {target_ip}...")
    # Iterate over the defined ports
    for port, service in ports_services.items():
        # Check if the port is open and grab a banner if available
        open_port, banner = scan_port(target_ip, port)
        if open_port:
            print(f"Port {port} ({service}) is OPEN.")
            print(f"Banner: {banner}")
        else:
            print(f"Port {port} ({service}) is closed or filtered.")

# Run the script
if __name__ == "__main__":
    main()
