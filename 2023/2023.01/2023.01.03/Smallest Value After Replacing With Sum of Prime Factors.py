def di(x):
    result = x
    arr = []
    while x != 1:
        for i in range(2, x + 1):
            if x % i == 0:
                x //= i
                arr.append(i)
                break
    if len(arr) >= 2:
        return di(sum(arr))
    else:
        return result


def smallestValue(n: int) -> int:
    return type(di(n))




print(smallestValue(15))
