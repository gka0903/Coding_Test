def solution(nums):
    n_min = 1e9
    n_max = -1e9
    l = len(nums)
    min_ = []
    max_ = []
    # min_
    for i in range(l):
        if n_min > nums[i]:
            n_min = nums[i]
        min_.append(n_min)
    # max_
    for i in range(l - 1, -1, -1):
        if n_max < nums[i]:
            n_max = nums[i]
        max_.append(n_max)
    # 비교 반복문
    for i in range(1, l - 1):
        if min_[i] < nums[i] < max_[l - i - 1]:
            return True
    return False


print(solution([4, 5, 2147483647, 1, 2]))
