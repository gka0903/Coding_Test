from collections import deque


def search(nums, target):
    if target not in nums:
        return -1
    nums = deque(nums)
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            print(nums[i], i, nums[i + 1])
            rotate = (len(nums) - 1) - i
            break
    for _ in range(rotate):
        nums.rotate()
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid, left, right)
        if nums[mid] == target:
            if mid - rotate >= 0:
                return mid - rotate
            else:
                return len(nums) + (mid - rotate)
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
