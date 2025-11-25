import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    q = deque([])
    stack = []

    for j in enumerate(s):
        q.append(j)
        stack.append(j[1])

    stack.sort()
    cnt = 1
    while q:
        d = q.popleft()

        if d[1] == stack[-1]:
            if d[0] == m:
                print(cnt)
                break
            else:
                cnt += 1
            stack.pop()
        else:
            q.append(d)
