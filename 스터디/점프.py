import sys

input = sys.stdin.readline
N = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
maps = []

for i in range(N):
    maps.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if maps[i][j] == 0:
            break

        ny = i + maps[i][j]
        nx = j + maps[i][j]

        if 0 <= ny < N:
            dp[ny][j] += dp[i][j]

        if 0 <= nx < N:
            dp[i][nx] += dp[i][j]

print(dp[-1][-1])
