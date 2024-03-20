def solution1(nums):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    print("solution1 : ", nums)


def solution2(nums):
    # 포인터를 3개
    # 0, 1, 2의 포인터를 잡고 1의 포인터는 순환 0, 2의 포인터는 조건부

    p0 = 0
    p1 = 0
    p2 = len(nums) - 1

    while p1 <= p2:
        if nums[p1] == 0:
            nums[p0], nums[p1] = nums[p1], nums[p0]
            p0 += 1
        if nums[p1] == 2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 -= 1
            continue
        p1 += 1

    print("solution2 : ", nums)


solution2([1, 2, 0])
solution2([2, 0, 2, 1, 1, 0])
# solution1([2, 0, 2, 1, 1, 0])
