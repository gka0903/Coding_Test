def subarraySum(nums, k):
    answer = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i + j + 1 > len(nums):
                break
            if sum(nums[j:i + j + 1]) == k:
                answer += 1
    return answer


print(subarraySum([1, 1, 1], 2))
