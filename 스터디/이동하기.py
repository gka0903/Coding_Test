import sys

input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
dp = [[0] * M for _ in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    maps.append(l)

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[i][j] = maps[i][j]

        if i >= 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + maps[i][j])

        if j >= 1:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + maps[i][j])

        if i >= 1 and j >= 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + maps[i][j])

print(dp[-1][-1])
