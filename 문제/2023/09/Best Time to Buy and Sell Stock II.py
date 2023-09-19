def sol(prices):
    dp = [0] * (len(prices) + 1)
    sell_index = len(prices)
    max_gain = 0
    check = 0

    for i in range(1, len(prices)):
        for j in range(i - 1, -1, -1):
            gain = prices[i] - prices[j]
            dp[i] = max(dp[i], gain)
            if j == sell_index:
                check = dp[i]
        dp[i] = max(check + dp[sell_index], dp[i])
        if max_gain < dp[i]:
            max_gain = dp[i]
            sell_index = i

    return dp


print(sol([7, 1, 5, 3, 6, 4]))
