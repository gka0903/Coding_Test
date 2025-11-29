def solution(n, k, b, arr):
    answer = 0
    status = [1] * n

    for i in arr:
        status[i - 1] = 0

    s, e, bcount, mincount = 0, 0, 0, 0

    while e < k:
        if status[e] == 0:
            bcount += 1
        e += 1
    mincount = bcount

    while e < n:
        if status[e] == 0:
            bcount += 1
        if status[s] == 0:
            bcount -= 1
        mincount = min(bcount, mincount)
        s += 1
        e += 1

    answer = mincount

    return answer
