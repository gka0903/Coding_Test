from itertools import combinations


def solution(numbers):
    arr = combinations(numbers, 2)
    answer = []
    for i in arr:
        num = i[0] + i[1]
        if num not in answer:
            answer.append(num)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
