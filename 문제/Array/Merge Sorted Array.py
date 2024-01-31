def solution(nums1, m, nums2, n):
    n1_index = m - 1
    n2_index = n - 1
    target = m + n - 1

    while n2_index >= 0:
        if nums1[n1_index] > nums2[n2_index]:
            nums1[target] = nums1[n1_index]
            n1_index -= 1
        else:
            nums1[target] = nums2[n2_index]
            n2_index -= 1
        target -= 1

    # n2가 남아 있을때
    while 0 <= n2_index:
        nums1[target] = nums2[n2_index]
        n2_index -= 1
        target -= 1
    return nums1


print(solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


# 오답
def solution1(nums1, m, nums2, n):
    zero_index = m
    for i in range(n):
        target = nums2[i]
        for j in range(m + n):
            if target <= nums1[j]:
                target, nums1[j] = nums1[j], target
        nums1[zero_index] = target
        zero_index += 1
    return nums1
