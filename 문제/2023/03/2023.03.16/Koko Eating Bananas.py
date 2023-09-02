def check(piles, k, h):
    a = 0
    for i in piles:
        if i % k == 0:
            a += i // k
        else:
            a += i // k + 1
    if a <= h:
        return True
    else:
        return False


def minEatingSpeed(piles, h):
    if len(piles) == 1:
        return piles[0]
    piles.sort()
    left = 0
    right = piles[-1]
    arr = []

    while left <= right:
        mid = (left + right) // 2
        if mid == 0:
            break
        c = check(piles, mid, h)
        if c:
            arr.append(mid)
            right = mid - 1
        else:
            left = mid + 1

    return min(arr)


print(minEatingSpeed([3, 6, 7, 11], 18))
