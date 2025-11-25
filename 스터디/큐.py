import sys
from collections import deque

input = sys.stdin.readline

q = deque([])


def push(X):
    q.append(X)


def pop():
    if not q:
        print(-1)
    else:
        print(q.popleft())


def size():
    print(len(q))


def empty():
    if not q:
        print(1)
    else:
        print(0)


def front():
    if not q:
        print(-1)
    else:
        print(q[0])


def back():
    if not q:
        print(-1)
    else:
        print(q[-1])


N = int(input())

for i in range(N):
    command = input().split()

    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "front":
        front()
    elif command[0] == "back":
        back()
