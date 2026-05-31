# Educational use only. Only scan systems you own or have permission to test. This script scans localhost (127.0.0.1) only.

# Import the built-in socket library so we can attempt TCP connections without external dependencies.
import socket

# Define the scan target as localhost, meaning this script only checks the current machine.
target_host = "127.0.0.1"

# Define the specific ports we want to check for common local services.
ports_to_scan = [22, 80, 443, 3306, 8080, 8443]

# Map each port number to a friendly service name so the output is easier to understand.
service_names = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
}

# Keep a counter of open ports so we can print a useful summary at the end.
open_count = 0

# Loop through each port in the list and test whether a TCP connection succeeds.
for port in ports_to_scan:
    # Look up the friendly service name for this port, or use "Unknown" if it is not listed.
    service_name = service_names.get(port, "Unknown")

    # Create a TCP socket using a context manager so it closes automatically after each check.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Set a short timeout so closed or filtered ports do not make the script wait too long.
        client_socket.settimeout(0.5)

        try:
            # Attempt to connect to the target host and port; success usually means the port is open.
            client_socket.connect((target_host, port))

            # Count the open port so the final summary is accurate.
            open_count += 1

            # Print the open result using the required output format.
            print(f"[OPEN]   Port {port} — {service_name}")
        except (ConnectionRefusedError, socket.timeout, TimeoutError, OSError):
            # Treat refused connections, timeouts, and socket errors as closed for this beginner demo.
            print(f"[CLOSED] Port {port} — {service_name}")

# Count how many ports were checked so the summary can show the total scan size.
total_checked = len(ports_to_scan)

# Print the final scan summary with the number of open ports found.
print(f"Scan complete. {open_count} port(s) open out of {total_checked} checked.")
