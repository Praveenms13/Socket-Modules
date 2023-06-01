import socket as s

hostIP = '0.0.0.0'#s.gethostbyname(s.gethostname())
port = int(input("Enter port number: "))

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind((hostIP, port))
server.listen()
print("TCP Server Started")
print(f"Waiting for a connection, Host IP: {hostIP}, Listening on Port: {port}")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr[0]}:{addr[1]}")
    conn.sendall("Welcome to Praveen's Server (TCP Server)".encode("utf-8"))
    print("Waiting for Request Data...")
    data = conn.recv(1024)
    while data:
        print(f"Message From {addr[0]}:{addr[1]} => {data.decode('utf-8')}")
        # conn.sendall(data.upper())  # Send the data back to the client
        data = conn.recv(1024)
