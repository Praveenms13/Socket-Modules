import socket as s
from threading import Thread

resp = """
HTTP/1.1 200 OK
Age: 230428
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Thu, 08 Jun 2023 09:06:44 GMT
Etag: "3147526947+gzip"
Expires: Thu, 15 Jun 2023 09:06:44 GMT
Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
Server: ECS (dcb/7FA3)
Vary: Accept-Encoding
X-Cache: HIT
Content-Length: 1256
Connection: close

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

HOST = "127.0.0.1"
PORT = 2000


class sIncomingThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print(f"Thread {addr[0]}:{addr[1]} started...")

    def run(self):
        self.conn.sendall(resp.encode("utf-8"))
        # data = self.conn.recv(1024)
        # while data:
        #     print("{}: ".format(self.addr[0]) + data.decode(), end="")
        #     data = self.conn.recv(1024)


server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

while True:
    print("waiting for new connection...")
    conn, addr = server.accept()
    print(f"Connection received from {addr[0]}:{addr[1]}")
    sIncomingThread(conn, addr).start()
