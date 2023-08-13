def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1

    x = m - 1
    y = n - 1
    return fac(x + y) // (fac(x) * fac(y))


print(uniquePaths(1, 2))
