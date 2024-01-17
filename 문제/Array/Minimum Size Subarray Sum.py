def solution(target, nums):
    index_left, total = 0, 0
    res = float("inf")

    for index_right in range(len(nums)):
        total += nums[index_right]
        while total >= target:
            res = min(index_right - index_left + 1, res)
            total -= nums[index_left]
            index_left += 1
    return res


print(solution(7, [2, 3, 1, 2, 4, 3]))
