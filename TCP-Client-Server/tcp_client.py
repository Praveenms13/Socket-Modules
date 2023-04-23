import socket as s

host = s.gethostname()
hostIP = s.gethostbyname(host)
port = int(input("Enter port number: "))

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect((hostIP, port))  # Connect to the hostIP variable
data = client.recv(1024)

print(f"Welcome Message: {data.decode()} from host: {hostIP}")

while True:
    data = input("Enter data to send (Request): ")
    client.sendall(data.encode())
    if data == "exit":
        break
    else:
        data = client.recv(1024)
        print(f"Data from server (Response): {data.decode()}")

client.close()
