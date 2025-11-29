import sys
from collections import deque

input = sys.stdin.readline
maps = []
N = int(input())

for i in range(N):
    l = list(input().strip())
    maps.append(l)

visit = [[False for _ in range(len(maps[0]))] for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

v1 = [row[:] for row in visit]
v2 = [row[:] for row in visit]
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(len(maps[0])):
        if not v1[i][j]:
            q = deque([(i, j)])
            v1[i][j] = True
            cnt1 += 1
            while q:
                y, x = q.popleft()

                for dy, dx in d:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < N and 0 <= nx < len(maps[0]):
                        if not v1[ny][nx]:
                            if maps[ny][nx] == maps[i][j]:
                                v1[ny][nx] = True
                                q.append((ny, nx))

        if not v2[i][j]:
            q = deque([(i, j)])
            v2[i][j] = True
            cnt2 += 1
            while q:
                y, x = q.popleft()
                color = False

                if maps[y][x] == "R" or maps[y][x] == "G":
                    color = True

                for dy, dx in d:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < N and 0 <= nx < len(maps[0]):
                        if not v2[ny][nx]:
                            if color:
                                if maps[ny][nx] == "R" or maps[ny][nx] == "G":
                                    v2[ny][nx] = True
                                    q.append((ny, nx))
                            else:
                                if maps[ny][nx] == "B":
                                    v2[ny][nx] = True
                                    q.append((ny, nx))

print(cnt1, cnt2)
