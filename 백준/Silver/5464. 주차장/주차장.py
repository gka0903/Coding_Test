import sys
from collections import defaultdict, deque

input = sys.stdin.readline
d = defaultdict(int)
q = deque([])
N, M = map(int, input().split())
parking = []
parking_count = 0
parking_place = defaultdict(int)
result = 0

for _ in range(N):
    parking.append([int(input()), False])

for i in range(1, M + 1):
    d[i] = int(input())


def park(n):
    global result, parking_count

    for i in range(N):
        if not parking[i][1]:
            result += d[n] * parking[i][0]
            parking_place[n] = i
            parking[i][1] = True
            parking_count += 1
            break


for _ in range(M * 2):
    number = int(input())

    if number > 0:
        q.append(number)

        while q and parking_count < N:
            num = q.popleft()
            park(num)
    else:
        idx = parking_place[-number]
        parking_count -= 1
        parking[idx][1] = False

        if q:
            num = q.popleft()
            park(num)

print(result)
