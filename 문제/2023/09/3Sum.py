def threeSum(nums):
    nums.sort()
    result = []
    for target in range(len(nums) - 1, 1, -1):
        first = 0
        end = target - 1
        while first < end:
            s_1 = nums[first] + nums[end] + nums[target]
            if s_1 == 0:
                if [nums[first], nums[end], nums[target]] not in result:
                    result.append([nums[first], nums[end], nums[target]])
                end -= 1
            elif s_1 > 0:
                end -= 1
            else:
                first += 1
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
