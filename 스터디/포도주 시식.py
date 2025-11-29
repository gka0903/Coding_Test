N = int(input())

w = [0]
dp = [0 for _ in range(N + 1)]

for _ in range(N):
    w.append(int(input()))

dp[1] = w[1]

if N > 1:
    dp[2] = w[1] + w[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i])


print(dp[-1])
