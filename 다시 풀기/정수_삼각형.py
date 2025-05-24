def solution(triangle):
    dp = [row[:] for row in triangle]
    for a in range(len(triangle) - 1):
        for b in range(len(triangle[a])):
            for c in range(2):
                fu_num = dp[a][b] + triangle[a + 1][b + c]
                if fu_num > dp[a + 1][b + c]:
                    dp[a + 1][b + c] = fu_num

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
