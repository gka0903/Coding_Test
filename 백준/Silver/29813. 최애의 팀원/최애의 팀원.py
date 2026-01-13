import sys
from collections import deque

input = sys.stdin.readline
q = deque([])
N = int(input())

for _ in range(N):
    c, n = input().split()
    q.append([c, int(n)])

while q:
    l = len(q)

    if l == 1:
        print(q.popleft()[0])
        break

    name, number = q.popleft()
    number = (number - 1) % (l - 1)

    for i in range(number):
        q.append(q.popleft())

    q.popleft()
