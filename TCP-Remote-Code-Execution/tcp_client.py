import socket as s

hostIP = '172.20.19.159'#s.gethostbyname(s.gethostname())
port = int(input("Enter port number: "))

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect((hostIP, port))  # Connect to the hostIP variable
data = client.recv(1024)

print(f"Welcome Message: {data.decode('utf-8')} from host: {hostIP}")

while True:
    data = input("Enter data to send (Request): ")
    client.sendall(data.encode("utf-8"))
    if data == "exit":
        break
    # else:
    #     data = client.recv(1024)
    #     print(f"Data from server (Response): {data.decode('utf-8')}")

client.close()
