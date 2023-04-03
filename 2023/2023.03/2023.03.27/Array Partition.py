def arrayPairSum(nums):
    nums.sort()
    answer = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            print(i)
            answer += nums[i]
    return answer


print(arrayPairSum([1, 4, 3, 2]))
