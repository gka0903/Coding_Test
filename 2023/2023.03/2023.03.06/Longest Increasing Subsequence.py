def lengthOfLIS(nums):
    check = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                check[i] = max(check[i], check[j] + 1)
    return max(check)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
