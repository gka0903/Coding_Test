import math


def solution(denum1, num1, denum2, num2):
    down = num1 * num2
    up = denum1 * num2 + denum2 * num1
    g = math.gcd(up, down)
    answer = [up // g, down // g]
    print(up, down)
    print(g)

    return answer



print(solution(9, 2, 1, 3))
