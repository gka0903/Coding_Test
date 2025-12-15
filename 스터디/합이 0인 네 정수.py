import sys

input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_count = {}
for a in A:
    for b in B:
        s = a + b
        if s in ab_count:
            ab_count[s] += 1
        else:
            ab_count[s] = 1

result = 0
for c in C:
    for d in D:
        target = -(c + d)

        if target in ab_count:
            result += ab_count[target]

print(result)
