#! /bin/python3

import socket as s
from threading import Thread

HOST = "0.0.0.0"
PORT = 3077
resp = """HTTP/1.1 200 OK
Accept-Ranges: bytes
Age: 472111
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Tue, 18 Apr 2023 14:58:32 GMT
Etag: "3147526947"
Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
Content-Length: 100000

<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
"""


class ClientThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print(f"Thread {addr[0]}:{addr[1]} started....")

    def run(self):
        self.conn.sendall(resp.encode("utf-8"))
        # self.conn.sendall("Welcome to praveen's server\n".encode())
        # print("Waiting for data...")
        # data = self.conn.recv(1024)
        # while data:
        #     print(
        #         f"From {self.addr[0]}:{self.addr[1]}, Received data: {data.decode()}",
        #         end="",
        #     )
        #     data = self.conn.recv(1024)


sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sck.bind((HOST, PORT))
sck.listen()
while True:
    print(f"Waiting for a Connection, Listening on {HOST}:{PORT}")
    conn, addr = sck.accept()
    print(f"Connected by {addr[0]} on {addr[1]} backport")
    ClientThread(conn, addr).start()
