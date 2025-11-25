import sys
from collections import deque

input = sys.stdin.readline
q = deque([])

N, K = map(int, input().split())

for i in range(1, N + 1):
    q.append(i)

cnt = 0
stack = []
while q:
    cnt += 1
    p = q.popleft()

    if cnt == K:
        stack.append(p)
        cnt = 0
    else:
        q.append(p)

print('<', end="")
for i in range(len(stack)):
    print(stack[i], end="")
    if i == len(stack) - 1:
        print('>', end="")
    else:
        print(', ', end="")
