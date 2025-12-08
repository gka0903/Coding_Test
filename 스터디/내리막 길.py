import sys

input = sys.stdin.readline
M, N = map(int, input().split())
m = []
dp = [[0 for _ in range(N)] for _ in range(M)]
d = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def dfs(y, x, cnt):
    dp[y][x] += cnt

    if y == M - 1 and x == N - 1:
        return

    for dy, dx in d:
        ny, nx = dy + y, dx + x

        if 0 <= ny < M and 0 <= nx < N:
            if m[ny][nx] < m[y][x]:
                dfs(ny, nx, dp[y][x])


for _ in range(M):
    li = list(map(int, input().split()))
    m.append(li)

dfs(0, 0, 1)

print(dp)
