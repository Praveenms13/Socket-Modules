#! /bin/python3

import socket as s

HOST = '0.0.0.0'
PORT = 3074

sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sck.bind((HOST, PORT))
sck.listen()
print(f"Waiting for a Connection, Listening on {HOST}:{PORT}")
conn, addr = sck.accept()
print(f"Connected by {addr[0]} and {addr[1]}")
conn.sendall("Welcome to praveen's server\n".encode())
print("Waiting for data...")
data = conn.recv(1024)
while data:
    print(f"Received data: {data.decode()}", end='')
    data = conn.recv(1024)