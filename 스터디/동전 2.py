import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = set()

for _ in range(n):
    A = int(input())
    coins.add(A)


s = min(coins)
dp = [10001] * (k + 1)
dp[0] = 0

for i in range(s, k + 1):
    for j in coins:

        if j <= i:
            dp[i] = min(dp[i - j] + 1, dp[i])

if dp[-1] != 10001:
    print(dp[-1])
else:
    print(-1)
