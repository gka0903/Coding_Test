def solution(nums):
    first_index = 0
    last_index = len(nums) - 1
    while first_index < last_index:
        pivot = (first_index + last_index) // 2
        if nums[pivot] < nums[pivot + 1]:
            first_index = pivot + 1
        else:
            last_index = pivot

    return first_index


print(solution([1, 2, 3, 1]))
