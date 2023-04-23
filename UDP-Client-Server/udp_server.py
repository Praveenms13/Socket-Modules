import socket as s

host = s.gethostname()
hostIP = s.gethostbyname(host)
port = int(input("Enter port number: "))

server = s.socket(s.AF_INET, s.SOCK_DGRAM)
server.bind((hostIP, port))
print("UDP server started\n")
print(f"Waiting for a connection, Host IP: {hostIP}, Listening on Port: {port}")

while True:
    data, addr = server.recvfrom(1024)
    print(f"Connected by {addr[0]}:{addr[1]}")
    print("Waiting for Request Data...")
    print(f"Message From {addr[0]}:{addr[1]} => {data.decode('utf-8')}")
    # Send the received message back to the client, converted to uppercase
    # server.sendto(data.upper(), addr)
