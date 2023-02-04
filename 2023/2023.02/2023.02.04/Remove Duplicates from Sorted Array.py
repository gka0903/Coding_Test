def removeDuplicates(nums):
    for i in reversed(range(1, len(nums))):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
    return len(nums)


print(removeDuplicates([1, 1, 2]))
