def solution(nums):
    if sum(nums) % 2 != 0:
        return False
    target = sum(nums) // 2
    dp = set()
    dp.add(0)
    for i in range(len(nums)):
        next_dp = set()
        for j in dp:
            next_dp.add(j + nums[i])
            next_dp.add(j)
        dp = next_dp
    return True if target in dp else False


print(solution([1, 5, 11, 5]))
