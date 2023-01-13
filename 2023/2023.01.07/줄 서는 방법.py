import itertools


def solution(n, k):
    answer = []
    arr = [i for i in range(1, n + 1)]
    print(arr)
    nPr = itertools.permutations(arr, n)
    nPrArr = list(nPr)
    return list(nPrArr[k - 1])


print(solution(3, 5))
