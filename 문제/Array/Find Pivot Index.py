def solution(nums):
    right_s = sum(nums)
    left_s = 0
    prev_ = 0
    for i in range(len(nums)):
        pivot = nums[i]
        right_s -= pivot
        left_s += prev_
        if left_s == right_s:
            return i
        prev_ = pivot
    return -1


print(solution([1, 2, 0, 3]))
