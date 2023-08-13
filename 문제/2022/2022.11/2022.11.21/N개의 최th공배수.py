import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def solution(arr):
    answer = 0
    l = 1
    for i in arr:
        l = math.lcm(l, i)

    return l


print(solution([2, 6, 8, 14]))
