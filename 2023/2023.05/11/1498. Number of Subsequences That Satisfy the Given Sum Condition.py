def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


def combination(n, r):
    return int(factorial(n) / (factorial(n - r) * factorial(r)))


def solution(nums, target):
    nums.sort()
    num_min = nums[0]
    for i in range(len(nums) - 1, 0, -1):
        if num_min + nums[i] <= target:
            num_max = i + 1
            break
    result = 0
    for i in range(1, num_max + 1):
        if i == 1:
            continue
        result += combination(num_max, i)
    return result


print(solution([3, 5, 6, 7], 9))
