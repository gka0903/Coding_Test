def search(nums, target):
    low = 0
    height = len(nums) - 1

    while low <= height:
        mid = (low + height) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            height = mid - 1
        else:
            low = mid + 1


print(search([-1, 0, 3, 5, 9, 12], 9))
