def solution(nums):
    start = 1
    end = 1
    m = -10
    for i in range(len(nums)):
        start *= nums[i]
        end *= nums[len(nums) - 1 - i]
        m = max(start, end, m)
        if start == 0:
            start = 1
        if end == 0:
            end = 1

    return m


print(solution([-2]))
