import heapq
import sys

input = sys.stdin.readline
h = heapq
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_h = []
min_h = []
result = 0

for i in range(N):
    h.heappush(max_h, -B[i])
    h.heappush(min_h, A[i])

for i in range(N):
    result += -h.heappop(max_h) * h.heappop(min_h)

print(result)
