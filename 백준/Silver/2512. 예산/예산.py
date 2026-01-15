import sys

input = sys.stdin.readline
N = int(input())

budgets = list(map(int, input().split()))
total = int(input())
s, e = 0, max(budgets)
result = s


def check(mid):
    money = 0

    for b in budgets:
        if b < mid:
            money += b
        else:
            money += mid

    return money <= total


while s <= e:
    m = (s + e) // 2

    if check(m):
        s = m + 1
        result = m
    else:
        e = m - 1

print(result)
