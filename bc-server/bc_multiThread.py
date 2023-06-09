# Full Duplux Process communication

from subprocess import Popen, STDOUT, PIPE
from threading import Thread


class outputThread(Thread):
    def __init__(self, cmd):
        Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        while self.cmd.poll() is None:
            print(self.cmd.stdout.readline().decode().strip())


cmdexec = Popen(["bc", "-q"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
out_t = outputThread(cmdexec)
out_t.start()
while cmdexec.poll() is None:
    cmd = input("> ")
    cmd = cmd + "\n"
    cmdexec.stdin.write(cmd.encode())
    cmdexec.stdin.flush()
