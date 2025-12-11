N = int(input())
l = list(map(int, input().split()))
dp = [1] * len(l)

for i in range(1, len(l)):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
