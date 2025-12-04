N = int(input())

dp = [0] * (N + 1)
dp[N - 1] = 1
dp[N - 2] = 2

for i in range(N - 3, -1, -1):
    dp[i] = min(dp[i + 1] + 1, dp[i + 3] + 1)

if dp[0] % 2 == 0:
    print("CY")
else:
    print("SK")
