import sys

input = sys.stdin.readline
d, n, m = map(int, input().split())
lands = []

for i in range(n):
    land = int(input())
    lands.append(land)
lands.sort()

start, end = 1, d

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    prev = lands[0]

    for i in range(len(lands)):
        now = lands[i]
        dist = prev - now
