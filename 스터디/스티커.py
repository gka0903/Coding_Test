T = int(input())

for _ in range(T):
    N = int(input())
    up_sticker = list(map(int, input().split()))
    down_sticker = list(map(int, input().split()))
    up_dp = [0] * N
    down_dp = [0] * N

    for i in range(N):
        if i == 0:
            up_dp[0] = up_sticker[0]
            down_dp[0] = down_sticker[0]

        if i == 1:
            up_dp[1] += down_sticker[0] + up_sticker[1]
            down_dp[1] += up_sticker[0] + down_sticker[1]

        if i >= 2:
            prev_ = max(up_dp[i - 2], down_dp[i - 2])
            up_dp[i] = max(up_sticker[i] + down_dp[i - 1], prev_ + up_sticker[i])
            down_dp[i] = max(down_sticker[i] + up_dp[i - 1], prev_ + down_sticker[i])

    print(max(up_dp[-1], down_dp[-1]))
