def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[left] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([3, 5, 1], 3))
