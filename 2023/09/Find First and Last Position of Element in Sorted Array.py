def solution(nums, target):
    res = [-1, -1]
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            res[0] = mid
            high = mid - 1

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            res[1] = mid
            low = mid + 1
    return res


print(solution([5, 7, 7, 8, 8, 10], 8))
