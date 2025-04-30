def solution(nums, k):
    for i in range(k):
        m = max(nums)
        index = nums.index(m)
        nums[index] = int(m ** 0.5)
    return sum(nums)


print(solution([25, 64, 9, 4, 100], 4))
