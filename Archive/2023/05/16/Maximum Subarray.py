def solution(nums):
    s = sum(nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
        s = max(s, sum(nums[left:right + 1]))
    while left < right:
        if nums[left] <= nums[right]:
            left += 1
        else:
            right -= 1
        s = max(s, sum(nums[left:right + 1]))
    return s


print(solution([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))
