cash = [0] * 100001


def solution(x):
    if x == 1 or x == 2:
        return 1
    if cash[x] != 0:
        return cash[x]

    cash[x] = solution(x - 1) + solution(x - 2)

    return cash[x] % 1234567


print(solution(100))
