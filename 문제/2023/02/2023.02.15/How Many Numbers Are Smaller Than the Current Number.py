def smallerNumbersThanCurrent(nums):
    nums_len = len(nums)
    answer = [0] * nums_len
    for i in range(nums_len):
        for j in range(nums_len):

            if nums[i] > nums[j]:
                answer[i] += 1
    return answer


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
