from itertools import combinations


def solution(numbers):
    m = 0
    com = list(combinations(numbers, 2))
    print(com)
    for i in com:
        m = max(m, i[0] * i[1])

    return m


print(solution([1, 2, -3, 4, -5]))
