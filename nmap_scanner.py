# pip install python-nmap
import nmap

# inherits all attributes from the port scanner of the nmap library
scanner = nmap.PortScanner

print("Welcome to Port Scanner")
print("-" * 23)

ip = input("Enter the IP: ")
type(ip)

# selecting the scanner option for scanning
menu = input(""""\n Choose the type of scan
            1 -> SYN
            2 -> UDP
            3 -> Intense
            Enter a number: """)

if menu == 1:
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Open Ports: ", scanner[ip]['tcp'].keys())
    