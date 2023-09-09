def solution_1(coins, amount):
    if amount == 0:
        return 0
    dp = [amount + 1] * (amount + 1)

    for i in coins:
        for j in range(1, len(dp)):
            if i < j:
                if dp[j - i] != amount + 1:
                    num = dp[j - i] + 1
                else:
                    num = dp[j]
            elif i == j:
                num = 1
            else:
                num = dp[j]
            dp[j] = min(dp[j], num)

    if dp[-1] == (amount + 1):
        return -1
    else:
        return dp[-1]


print(solution_1([2], 3))
