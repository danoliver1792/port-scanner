import socket

ip = input("Enter the Host or IP: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input("Enter the port: ")))
    count += 1

for port in ports:
    # using IPv4 communications and creating a stream socket, using TCP communications
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print(f"{str(port)} >>> The port is open")
    else:
        print(f"{str(port)} >>> The port is close")

print("Scan Finished")

