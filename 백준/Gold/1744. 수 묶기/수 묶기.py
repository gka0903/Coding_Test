import sys

input = sys.stdin.readline

N = int(input())
plus, minus = [], []
result = 0

for _ in range(N):
    num = int(input())

    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort()
minus.sort()

for i in range(len(plus) - 1, -1, -2):
    if i == 0:
        result += plus[i]
        continue

    if plus[i] > 1 and plus[i - 1] > 1:
        result += plus[i] * plus[i - 1]
    else:
        result += plus[i] + plus[i - 1]

for i in range(0, len(minus), 2):
    if i == len(minus) - 1:
        result += minus[i]
        continue

    result += minus[i] * minus[i + 1]

print(result)
