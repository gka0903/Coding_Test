from functools import reduce


def maxProduct(nums):
    num_len = 1
    nums_len = len(nums)
    arr = []
    while num_len != nums_len + 1:
        for i in range(0, nums_len):
            num_arr = nums[i: i + num_len]
            arr.append(reduce(lambda x, y: x * y, num_arr))
        num_len += 1
    return max(arr)


print(maxProduct([2, -5, -2, -4, 3]))
