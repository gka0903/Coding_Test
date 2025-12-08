import sys

input = sys.stdin.readline
N, M = map(int, input().split())
pay = []

for i in range(N):
    num = int(input())
    pay.append(num)

s, e = max(pay), sum(pay)


def check(mid):
    cnt = 1
    money = mid

    for p in pay:

        if money < p:
            cnt += 1
            money = mid
        money -= p

    if cnt <= M:
        return True
    else:
        return False


target = None

while s <= e:
    m = (s + e) // 2

    if check(m):
        e = m - 1
        target = m
    else:
        s = m + 1

print(target)
