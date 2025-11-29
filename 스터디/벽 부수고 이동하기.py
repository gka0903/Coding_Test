from collections import deque

N, M = map(int, input().split())
f = []
wall = []
result = 2000

for i in range(N):
    l = []
    nums = list(map(int, input().strip()))
    f.append(nums)

    for j in range(M):
        if nums[j] == 1:
            wall.append((i, j))
print(wall)

for y, x in wall:
    f[y][x] = 0

    q = deque([(0, 0)])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    v = [[False for _ in range(M)] for _ in range(N)]
    v[0][0] = True
    cnt = 0
    check = False

    while q:
        cy, cx = q.popleft()

        if cy == N - 1 and cx == M - 1:
            check = True
            break

        for dy, dx in d:
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < N and 0 <= nx < M:
                if not v[ny][nx] and f[ny][nx] == 0:
                    cnt += 1
                    v[ny][nx] = True
                    q.append((ny, nx))

    f[y][x] = 1

    if check:
        result = min(cnt, result)


print(result)
