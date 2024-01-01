def solution(nums, target):
    dp = [0] * (target + 1)

    for i in nums:
        for j in range(1, target + 1):
            if j == i:
                dp[j] += 1
            if j > i:
                dp[j] += dp[j - i]

    return dp[-1]


print(solution([1, 2, 3], 4))
