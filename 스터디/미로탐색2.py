import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
result = 0
miro = []
for _ in range(N):
    row = list(map(int, input().rstrip()))
    miro.append(row)

visit = [[False for _ in range(M)] for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque([(0, 0, 1)])
visit[0][0] = True
while q:
    y, x, cnt = q.popleft()

    if y == N - 1 and x == M - 1:
        result = cnt
        break

    for dy, dx in dir:
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M:
            if not visit[ny][nx] and miro[ny][nx] == 1:
                visit[ny][nx] = True
                q.append((ny, nx, cnt + 1))

print(result)
