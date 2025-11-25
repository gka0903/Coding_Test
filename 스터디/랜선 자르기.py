import sys

input = sys.stdin.readline
s = 1
lan = []

K, N = map(int, input().split())
for i in range(K):
    n = int(input())
    lan.append(n)

e = max(lan)

while s <= e:
    m = (s + e) // 2
    cnt = 0
    for l in lan:
        cnt += l // m

    if cnt >= N:
        s = m + 1
    else:
        e = m - 1

print(e)
