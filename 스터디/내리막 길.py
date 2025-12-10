import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M, N = map(int, input().split())
m = []
dp = [[-1 for _ in range(N)] for _ in range(M)]
d = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def dfs(y, x):
    if y == M - 1 and x == N - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for dy, dx in d:
        ny, nx = dy + y, dx + x

        if 0 <= ny < M and 0 <= nx < N:
            if m[ny][nx] < m[y][x]:
                dp[y][x] += dfs(ny, nx)

    return dp[y][x]


for _ in range(M):
    li = list(map(int, input().split()))
    m.append(li)

dfs(0, 0)

print(dp[0][0])
