def solution(nums):
    prev = cur = max_sum = 0
    check_zero = True

    for i in range(len(nums)):
        if nums[i] == 1:
            cur += 1
        else:
            check_zero = False
            if max_sum < prev + cur:
                max_sum = prev + cur
            prev = cur
            cur = 0
    if max_sum < prev + cur:
        max_sum = prev + cur
    if check_zero:
        max_sum -= 1
    return max_sum


def solution2(nums):
    return 0


print(solution2([1, 1, 0, 1]))

# print(solution([1, 1, 0, 1]))
print(solution([1, 1, 1]))
