import socket
from subprocess import Popen, STDOUT, PIPE
from threading import Thread

host_ip = "0.0.0.0"
port = 1000
con = []


class OutputThread(Thread):
    def __init__(self, cmd, conn, addr):
        super().__init__()
        self.cmd = cmd
        self.conn = conn
        self.addr = addr

    def run(self):
        while self.cmd.poll() is None:
            try:
                self.conn.sendall(self.cmd.stdout.readline())
            except Exception as e:
                print(
                    f"Connection resest for => {self.addr[0]}:{self.addr[1]}\nError => {e}"
                )
                con.remove(self.addr[0])


class MathServerThread(Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        cmdexec = Popen(["bc"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        out_t = OutputThread(cmdexec, self.conn, self.addr)
        out_t.start()
        while cmdexec.poll() is None:
            try:
                cmd = self.conn.recv(4096)
                cmd = cmd.decode("utf-8").strip()
                if not cmd:
                    break
                if cmd == "kill" or cmd == "exit" or cmd == "quit":
                    cmdexec.kill()
                    break
                cmd = cmd + "\n"
                cmdexec.stdin.write(cmd.encode())
                cmdexec.stdin.flush()
            except Exception as e:
                print(f"{self.addr[0]}:{self.addr[1]}\nError => {e}")
                self.conn.close()
                con.remove(self.addr[0])


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_ip, port))
server.listen()
print("TCP Server Started")
while True:
    conn, addr = server.accept()
    if addr[0] in con:
        print("Connection Rejected {}:{}".format(addr[0], addr[1]))
        conn.close()
    else:
        con.append(addr[0])
        print("Connection received from {}:{}".format(addr[0], addr[1]))
        t = MathServerThread(conn, addr)
        t.start()
