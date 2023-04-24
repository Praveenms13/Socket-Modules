import socket as s

HOST = '127.0.0.1'
PORT = 3074

sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.connect((HOST, PORT))
print("Connected to server")

while True:
    message = input("Enter message: ")
    sck.sendall(message.encode())
    data = sck.recv(1024)
    print(f"Received response: {data.decode()}")
