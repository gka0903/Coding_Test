def maxSubArray(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s > nums[i]:
            nums[i] = s
        else:
            s = nums[i]
    return max(nums)
