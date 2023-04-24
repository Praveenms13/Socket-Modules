import socket

# Define server host and port
HOST = '172.20.16.104'
PORT = int(input('Enter port: '))

# Create client socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
# Continuously send messages to server
while True:
    # Get message input from user
    message = input('Enter message: ')

    # Send message to server
    client_socket.sendall(message.encode())

# Close client socket
client_socket.close()
