import sys

input = sys.stdin.readline
n = int(input())

s = 0
e = n
result = 0

while s <= e:
    m = (s + e) // 2

    if m * m >= n:
        e = m - 1
        result = m
    else:
        s = m + 1

print(result)
