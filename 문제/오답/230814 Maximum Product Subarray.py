from typing import List


def maxProduct(nums: List[int]) -> int:
    multiplication = nums[0]
    result = []
    for i in range(1, len(nums)):
        multiplication *= nums[i]
        if multiplication < nums[i]:
            result.append(nums[i])
        else:
            if multiplication >= 0:
                result.append(multiplication)
    multiplication = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        multiplication *= nums[i]
        if multiplication < nums[i]:
            result.append(nums[i])
        else:
            if multiplication >= 0:
                result.append(multiplication)
    return result


print(maxProduct([2, -5, -2, -4, 3]))
