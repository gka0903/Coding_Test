def solution(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            return abs(num)
        else:
            nums[index] = -nums[index]


print(solution([1, 3, 4, 2, 2]))
