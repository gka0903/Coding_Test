from itertools import combinations


def solution(nums):
    answer = 0
    items = list(combinations(nums, 3))
    for i in items:
        num = sum(i)
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            answer += 1
    return answer


print(solution([1, 2, 7, 6, 4]))
