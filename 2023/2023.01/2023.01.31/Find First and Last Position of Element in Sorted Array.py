def searchRange(nums, target):
    if target in nums:
        first_index = nums.index(target)
        last_index = 0
        for i in range(len(nums) - 1, first_index - 1, -1):
            if nums[i] == target:
                last_index = i
                break
        return [first_index, last_index]
    else:
        return [-1, -1]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
