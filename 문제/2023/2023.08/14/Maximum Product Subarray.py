from typing import List


def maxProduct(nums: List[int]) -> int:
    curMax, curMin = 1, 1
    res = nums[0]

    for n in nums:
        vals = (n, n * curMax, n * curMin)
        curMax, curMin = max(vals), min(vals)
        res = max(res, curMax)
        print("curMax curMin res ", curMax, " ", curMin, " ", res)

    return res


print(maxProduct([2, -5, -2, -4, 3]))
