def solution(land):
    dp = land
    n = len(land)

    for i in range(1, n):
        for j in range(4):
            dp[i][j] += max(dp[i - 1][k] for k in range(4) if k != j)

    return max(dp[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
