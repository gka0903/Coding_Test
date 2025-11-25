import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = []
for i in range(N):
    t = list(map(int, input().split()))
    tomato.append(t)

first = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            first.append((i, j))
q = deque([first])
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 0
while q:
    cur = q.popleft()
    new_tomato = []

    for i, j in cur:
        for di, dj in d:
            ni, nj = di + i, dj + j

            if 0 <= ni < N and 0 <= nj < M:
                if tomato[ni][nj] == 0:
                    tomato[ni][nj] = 1
                    new_tomato.append((ni, nj))

    if new_tomato:
        q.append(new_tomato)
    result += 1

check = True

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            check = False
            break

if check:
    print(result - 1)
else:
    print(-1)
