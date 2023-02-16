def kidsWithCandies(c, e):
    m = max(c)
    result = []
    for i in c:
        if e + i >= m:
            result.append(True)
        else:
            result.append(False)
    return result


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
