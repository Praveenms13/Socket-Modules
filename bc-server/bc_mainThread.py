# Since it is not threaded loop will not work here and also deadlock issue occurs in this
# Half Duplux process communication

from subprocess import Popen, STDOUT, PIPE

cmdexec = Popen(["bc", "-q"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)

while cmdexec.poll() is None:
    cmd = input("> ")
    cmd = cmd + "\n"
    cmdexec.stdin.write(cmd.encode())
    cmdexec.stdin.flush()
    print(cmdexec.stdout.readline().decode().strip())

# to detach readline in seperate thread to avoid deadlock

# from subprocess import Popen, STDOUT, PIPE
# from threading import Thread


# def readline(cmdexec):
#     while cmdexec.poll() is None:
#         print(cmdexec.stdout.readline().decode().strip())


# cmdexec = Popen(["bc", "-q"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
# thread1 = Thread(target=readline, args=(cmdexec,)).start()

# while cmdexec.poll() is None:
#     cmd = input("> ")
#     cmd = cmd + "\n"
#     cmdexec.stdin.write(cmd.encode())
#     cmdexec.stdin.flush()
