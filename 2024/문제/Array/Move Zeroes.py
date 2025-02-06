def solution(nums):
    zero_index = 0
    for num_index in range(len(nums)):
        if nums[num_index] != 0:
            nums[zero_index], nums[num_index] = nums[num_index], nums[zero_index]
            zero_index += 1
    for i in range(zero_index, len(nums)):
        nums[i] = 0
    return nums


print(solution([0, 1, 0, 3, 12]))
