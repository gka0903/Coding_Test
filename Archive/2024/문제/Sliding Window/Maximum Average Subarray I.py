# 연속하는 k만큼의 수들 중 평균이 가장 큰 것을 리턴
def solution1(nums, k):
    max_sum = 0
    l = len(nums)
    if l <= k:
        return sum(nums) / k
    for i in range(0, l - k + 1):
        s = sum(nums[i:i + k])
        if s > max_sum:
            max_sum = s
    return max_sum / k


def solution2(nums, k):
    cur_sum = sum(nums[:k])
    max_sum = cur_sum

    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum / k


print(solution2([1, 12, -5, -6, 50, 3], 4))
