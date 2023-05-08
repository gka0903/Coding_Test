def solution(nums):
    nums.sort()
    print(nums)
    if not nums:
        return 0
    count = 1
    arr = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        print(nums[i], nums[i - 1])
        if nums[i] - nums[i - 1] == 1:
            print(count)
            count += 1
        else:
            arr.append(count)
            count = 1
    arr.append(count)
    return max(arr)


print(solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
