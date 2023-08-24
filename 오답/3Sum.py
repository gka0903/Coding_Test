def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        numbers = nums[0:i] + nums[i + 1: len(nums)]
        left = 0
        right = len(numbers) - 1
        target = nums[i]
        while left < right:
            check = numbers[left] + numbers[right] + target
            if check == 0:
                s = sorted([numbers[left], numbers[right], target])
                if s not in result:
                    result.append(s)
                break
            elif check > 0:
                right -= 1
            else:
                left += 1
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
