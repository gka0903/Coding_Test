def pivotIndex(nums):
    for i in range(1, len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i
    return 0


print(pivotIndex([1, 7, 3, 6, 5, 6]))
