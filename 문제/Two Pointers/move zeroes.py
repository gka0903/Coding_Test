def solution(nums):
    zero1 = -1
    zero2 = -1

    for i in range(len(nums)):
        if nums[i] == 0:
            if zero1 == -1:
                zero1 = i
            elif zero2 == -1:
                zero2 = i
        else:
            if zero1 == -1:
                continue
            else:
                nums[i], nums[zero1] = nums[zero1], nums[i]
                if zero2 != -1:
                    zero1 += 1
                else:
                    zero1 = i
    return nums


print(solution([45192, 0, -659, -52359, -99225, -75991, 0, -15155, 27382, 59818, 0, -30645, -17025, 81209, 887, 64648]))
