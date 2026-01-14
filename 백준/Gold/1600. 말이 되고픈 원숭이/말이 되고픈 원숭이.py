import sys
from collections import deque

input = sys.stdin.readline

dy = [1, 0, -1, 0, 2, 2, -2, -2, 1, -1, 1, -1]
dx = [0, 1, 0, -1, 1, -1, 1, -1, 2, 2, -2, -2]
K = int(input())
W, H = map(int, input().split())
graph = []

for i in range(H):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]
q = deque([(0, 0, K)])
visited[0][0][K] = 0

while q:
    y, x, k = q.popleft()

    if y == H - 1 and x == W - 1:
        break

    for i in range(12):
        ny, nx = dy[i] + y, dx[i] + x
        nk = k

        if i > 3:
            if k > 0:
                nk -= 1
            else:
                break

        if 0 <= ny < H and 0 <= nx < W:
            if graph[ny][nx] != 1:
                if visited[ny][nx][nk] == -1:
                    visited[ny][nx][nk] = visited[y][x][k] + 1
                    q.append((ny, nx, nk))

result = float("inf")
for cnt in visited[H - 1][W - 1]:
    if cnt != -1:
        if result > cnt:
            result = cnt

if result == float("inf"):
    print(-1)
else:
    print(int(result))
