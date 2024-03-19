def solution(nums, target):
    point_one = 0
    point_two = len(nums) - 1
    s = sorted(nums)
    while point_one < point_two:
        result = s[point_one] + s[point_two]
        if result == target:
            index_one = nums.index(s[point_one])
            index_two = nums.index(s[point_two]) if not s[point_one] == s[point_two] else nums.index(s[point_two],
                                                                                                     index_one + 1)
            return [index_one, index_two]
        elif result < target:
            point_one += 1
        else:
            point_two -= 1
    return - 1


print(solution([3, 3], 6))
