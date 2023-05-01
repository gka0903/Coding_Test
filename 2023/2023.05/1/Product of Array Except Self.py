def solution(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        print(result, i, nums[i])
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
        print(result)

    return result


print(solution([1, 2, 3, 4]))
