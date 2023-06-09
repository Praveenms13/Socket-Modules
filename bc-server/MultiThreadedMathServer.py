import socket
from subprocess import Popen, STDOUT, PIPE
from threading import Thread

host_ip = "0.0.0.0"
port = 2000


class OutputThread(Thread):
    def __init__(self, cmd, conn):
        super().__init__()
        self.cmd = cmd
        self.conn = conn

    def run(self):
        while self.cmd.poll() is None:
            self.conn.sendall(self.cmd.stdout.readline())


class MathServerThread(Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        cmdexec = Popen(["bc"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        out_t = OutputThread(cmdexec, self.conn)
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
            except Exception as e:
                print(
                    f"Error message from => {self.addr[0]}:{self.addr[1]}\nError => {e}"
                )
            cmd = cmd + "\n"
            cmdexec.stdin.write(cmd.encode())
            cmdexec.stdin.flush()

        self.conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_ip, port))
server.listen()
print("TCP Server Started")
while True:
    conn, addr = server.accept()
    print("Connection received from {}:{}".format(addr[0], addr[1]))
    t = MathServerThread(conn, addr)
    t.start()
