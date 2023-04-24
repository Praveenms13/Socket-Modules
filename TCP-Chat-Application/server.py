import socket
import threading

HOST = '0.0.0.0'
PORT = int(input('Enter port: '))
MESSAGE_FORMAT = '{sender}: {message}'

def handle_client(conn, addr, clients):
    clients.append(conn)
    print(f'Client {addr} connected')

    while True:
        try:
            # Receive message from client
            message = conn.recv(1024).decode()
            print(f'Received message from {addr}: {message}')

            # Broadcast message to all connected clients
            for client in clients:
                if client != conn:
                    client.sendall(MESSAGE_FORMAT.format(sender=addr, message=message).encode())

            # Send response back to client
            response = 'Message received'
            conn.sendall(response.encode())

        except:
            # Remove client from list of connected clients
            clients.remove(conn)
            print(f'Client {addr} disconnected')
            conn.close()
            break

# Create server socket and listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'Server started on {HOST}:{PORT}')

# List to store connected clients
clients = []

while True:
    # Accept new connection and start new thread to handle it
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(conn, addr, clients)).start()
