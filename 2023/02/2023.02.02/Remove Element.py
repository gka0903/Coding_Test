def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


print(removeElement([3, 2, 2, 3], 3))
