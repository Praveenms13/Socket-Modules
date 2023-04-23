import socket as s

host = s.gethostname()
hostIP = s.gethostbyname(host)
port = int(input("Enter port number: "))

client = s.socket(s.AF_INET, s.SOCK_DGRAM)
# client.connect((hostIP, port))  # This will only work in tct client
print("UDP Client started\n")

while True:
    data = input("Enter data to send (Request): ")
    client.sendto(data.encode("utf-8"), (hostIP, port))
    if data == "exit":
        break
    # else:
    #     data, addr = client.recvfrom(1024)
    #     print(f"Data from server (Response): {data.decode('utf-8')}")
