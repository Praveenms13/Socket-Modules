import socket
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr

def start_server():
    hostIP = "0.0.0.0"
    port = int(input("Enter port number: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            print(f"Command From {addr[0]}:{addr[1]} => {data.decode('utf-8')}")
            print("Executing the command...")
            command = data.decode("utf-8")
            output = run_command(command)
            response = f"Output of the command:\n{output}".encode("utf-8")
            conn.sendall(response)
            data = conn.recv(1024)

start_server()
