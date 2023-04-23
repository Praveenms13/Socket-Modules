import socket as s

host = s.gethostname()
hostIP = s.gethostbyname(host)
port = int(input("Enter port number: "))

socketConn = s.socket(s.AF_INET, s.SOCK_STREAM)
socketConn.bind((hostIP, port))
socketConn.listen()

print(f"Waiting for a connection, Host IP: {hostIP}, Listening on Port: {port}")
while True:
    conn, addr = socketConn.accept()
    print(f"Connected by {addr[0]}: {addr[1]}")
    conn.sendall("Welcome to Praveen's Server".encode())
    print("Waiting for data...")
    data = conn.recv(1024)
    while data:
        print(f"Message From {hostIP}: {data.decode()}")
        conn.sendall(data.upper())  # Send the data back to the client
        data = conn.recv(1024)
