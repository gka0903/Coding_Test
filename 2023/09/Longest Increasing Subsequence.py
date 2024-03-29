def solution(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


print(solution([10, 9, 2, 5, 3, 7, 101, 18]))
