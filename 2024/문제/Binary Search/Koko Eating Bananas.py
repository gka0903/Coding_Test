import math


def solution(piles, h):
    l = 1
    r = max(piles)
    res = r
    while l <= r:
        k = (l + r) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        if hours > h:
            l = k + 1
        elif hours <= h:
            res = min(res, k)
            r = k - 1

    return res


print(solution([3, 6, 7, 11], 8))
