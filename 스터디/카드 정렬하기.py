import heapq
import sys

input = sys.stdin.readline
h = heapq
p = []
N = int(input())
result = 0

for i in range(N):
    n = int(input())
    h.heappush(p, n)

while len(p) >= 2:
    n1, n2 = h.heappop(p), h.heappop(p)
    s = n1 + n2
    result += s
    h.heappush(p, s)

print(result)
