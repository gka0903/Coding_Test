N = int(input())
T = [0]
P = [0]
dp = [0] * (N + 2)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N, 0, -1):

    # 일을 하지 않는다
    work_not_today = dp[i + 1]

    # 일을 한다
    # 가능시(t + 현재 날 < N)
    work_today = P[i] + dp[i + T[i]] if T[i] + i <= N + 1 else 0
    dp[i] = max(work_not_today, work_today)

print(dp[1])
