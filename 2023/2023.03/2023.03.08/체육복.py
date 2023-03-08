def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    c = lost & reserve
    lost = lost - c
    reserve = reserve - c
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
    return n - len(lost)


print(solution(8, [5, 6, 7, 8], [4, 7]))
