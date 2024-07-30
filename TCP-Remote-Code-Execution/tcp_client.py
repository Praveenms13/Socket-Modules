import socket

def start_client():
    hostIP = '172.20.19.159'  # s.gethostbyname(s.gethostname())
    port = int(input("Enter port number: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((hostIP, port))
    data = client.recv(1024)

    print(f"Welcome Message: {data.decode('utf-8')} from host: {hostIP}")

    while True:
        data = input("Enter the Command > ")
        client.sendall(data.encode("utf-8"))
        if data == "exit":
            break
        else:
            data = client.recv(1024)
            print(f"{data.decode('utf-8')}")

    client.close()

start_client()
