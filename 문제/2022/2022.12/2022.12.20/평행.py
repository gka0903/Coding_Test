def cal(dot1, dot2):
    dx = dot1[0] - dot2[0]
    dy = dot1[1] - dot2[1]
    return dy / dx


def solution(dots):
    dots.sort()
    print(dots)
    a, b, c, d = dots
    print(a, b, c, d)
    d1 = cal(a, b)
    d2 = cal(c, d)
    if d1 == d2:
        return 1
    return 0


print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
