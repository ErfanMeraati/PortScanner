import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
    3389: "RDP", 5432: "PostgreSQL", 6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt"
}

def scan_port(host, port, timeout=1):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return port, True
    except:
        return port, False

def scan(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[!] Could not resolve: {host}")
        return

    print(f"\n🔍 Scanning {host} ({ip})")
    print(f"   Ports: {min(ports)}–{max(ports)}")
    print(f"   Started: {datetime.now().strftime('%H:%M:%S')}")
    print("─" * 40)

    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as ex:
        futures = {ex.submit(scan_port, ip, p): p for p in ports}
        for f in as_completed(futures):
            port, is_open = f.result()
            if is_open:
                service = COMMON_PORTS.get(port, "Unknown")
                print(f"  [OPEN]  {port:<6} {service}")
                open_ports.append((port, service))

    print("─" * 40)
    print(f"  {len(open_ports)} open port(s) found.\n")
    return open_ports

def main():
    host = input("Host/IP: ").strip()
    mode = input("Scan mode — [1] Common  [2] 1-1024  [3] Full (1-65535): ").strip()

    if mode == "1":
        ports = list(COMMON_PORTS.keys())
    elif mode == "2":
        ports = range(1, 1025)
    elif mode == "3":
        ports = range(1, 65536)
    else:
        print("Invalid choice.")
        input()
        sys.exit()

    results = scan(host, ports)

    if results:
        save = input("Save results? (y/n): ").strip().lower()
        if save == "y":
            fname = f"scan_{host.replace('.','_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(fname, "w") as f:
                f.write(f"Host: {host}\n")
                for port, svc in sorted(results):
                    f.write(f"{port}\t{svc}\n")
            print(f"Saved to {fname}")
            input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
