import heapq
import sys

input = sys.stdin.readline
h = heapq
N = int(input())
result = 0

if N != 1:
    member = []
    m_number = 0
    target = int(input())

    for i in range(1, N):
        number = int(input())
        h.heappush(member, -number)

    while True:
        num = -h.heappop(member)

        if target > num:
            break

        result += 1
        target += 1
        h.heappush(member, -(num - 1))

print(result)
