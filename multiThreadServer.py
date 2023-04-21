#! /bin/python3

import socket as s
from threading import Thread

HOST = "0.0.0.0"
PORT = 3076

class ClientThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print (f"Thread {addr[0]}:{addr[1]} started....")
    def run(self):
        self.conn.sendall("Welcome to praveen's server\n".encode())
        print("Waiting for data...")
        data = self.conn.recv(1024)
        while data:
            print(f"From {self.addr[0]}:{self.addr[1]}, Received data: {data.decode()}", end="")
            data = self.conn.recv(1024)      

 
sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sck.bind((HOST, PORT))
sck.listen()
while True:
    print(f"Waiting for a Connection, Listening on {HOST}:{PORT}")
    conn, addr = sck.accept()
    print(f"Connected by {addr[0]} on {addr[1]} backport")
    ClientThread(conn, addr).start()
  