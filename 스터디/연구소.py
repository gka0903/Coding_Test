import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
m = []
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

for i in range(N):
    l = list(map(int, input().split()))
    m.append(l)

virus = [(i, j) for i in range(N) for j in range(M) if m[i][j] == 2]
empty = [(i, j) for i in range(N) for j in range(M) if m[i][j] == 0]
l = len(empty)

for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            a, b, c = empty[i], empty[j], empty[k]
            target = 0
            test_map = [row[:] for row in m]
            q = deque(row[:] for row in virus)

            for y, x in [a, b, c]:
                test_map[y][x] = 1

            while q:
                y, x = q.popleft()

                for dy, dx in dir:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < N and 0 <= nx < M:
                        if test_map[ny][nx] == 0:
                            test_map[ny][nx] = 2
                            q.append((ny, nx))

            for y in range(N):
                for x in range(M):
                    if test_map[y][x] == 0:
                        target += 1

            if target > result:
                result = target

print(result)
