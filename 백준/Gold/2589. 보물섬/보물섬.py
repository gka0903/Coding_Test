import sys
from collections import deque

input = sys.stdin.readline
H, W = map(int, input().split())
graph = [[] for _ in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(H):
    row = input().strip()

    for j in range(len(row)):
        graph[i].append(row[j])


def bfs(y, x):
    visit = [[False for _ in range(W)] for _ in range(H)]
    visit[y][x] = True
    q = deque([(y, x, 0)])
    result = 0

    while q:
        qy, qx, dist = q.popleft()

        if result < dist:
            result = dist

        for i in range(4):
            ny, nx = qy + dy[i], qx + dx[i]

            if 0 <= ny < H and 0 <= nx < W:
                if graph[ny][nx] != "W":
                    if not visit[ny][nx]:
                        visit[ny][nx] = True
                        q.append((ny, nx, dist + 1))

    return result


distance = 0
for i in range(H):
    for j in range(W):
        if graph[i][j] == "L":
            d = bfs(i, j)
            distance = max(d, distance)

print(distance)
