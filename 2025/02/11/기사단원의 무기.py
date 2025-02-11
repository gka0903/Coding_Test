import math


def find_measure(number):
    count = 0

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1 if i == number // i else 2
    return count


def solution(number, limit, power):
    result = 0

    for i in range(1, number + 1):
        p = find_measure(i)
        if p > limit:
            result += power
        else:
            result += p

    return result


print(solution(5, 3, 2))
