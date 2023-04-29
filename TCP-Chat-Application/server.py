import socket

host = socket.gethostname()
host_ip = socket.gethostbyname(host)
port = int(input("Enter port number: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_ip, port))
server.listen()

print("TCP Server Started")
print(f"Waiting for a connection, Host IP: {host_ip}, Listening on Port: {port}")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr[0]}:{addr[1]}")
    conn.sendall(b"Welcome to Praveen's Server (TCP Server)")
    print("Waiting for Request Data...")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Message From {addr[0]}:{addr[1]} => {data.decode()}")
        # conn.sendall(data.upper())  # Send the data back to the client
    conn.close()

server.close()
