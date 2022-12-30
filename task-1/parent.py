#!/usr/bin/python3
import os
import random
import sys


def fork():
    child = os.fork()
    if child > 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child}.')
    else:
        os.execl(sys.executable, sys.executable, "child.py", str(random.randint(5, 10)))


n = int(sys.argv[1])
for i in range(n):
    fork()

cnt = n
while cnt > 0:
    pid, status = os.wait()
    if status != 0:
        child = fork()
    else:
        print(f'Parent[{os.getpid()}]: Child with PID {pid} terminated. Exit Status {status}.')
        cnt = cnt - 1

os._exit(os.EX_OK)
