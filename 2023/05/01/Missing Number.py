def solution(nums):
    nums.sort()
    for i in range(0, len(nums) + 1):
        if i != nums[i]:
            return i


print(solution([9, 6, 4, 2, 3, 5, 7, 0, 1]))
