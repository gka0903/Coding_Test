def solution(nums):
    nums.sort()
    result = []
    for target in range(len(nums) - 1, 1, -1):
        first = 0
        end = target - 1
        while first < end:
            print(nums[first], nums[end], nums[target])
            s = nums[first] + nums[end] + nums[target]
            if s == 0:
                if [nums[first], nums[end], nums[target]] not in result:
                    result.append([nums[first], nums[end], nums[target]])
                end -= 1
            elif s > 0:
                end -= 1
            else:
                first += 1
    return result


print(solution([0, 0, 0]))
