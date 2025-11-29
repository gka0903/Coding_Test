import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
h = heapq
N, M = map(int, input().split())
heap = []

# 제약 조건 있는 수들
priority = [0 for _ in range(N + 1)]

# 먼저 나오면 제약을 줄이는 수들
reduce = defaultdict(list)

# 제약 조건 확인
for i in range(M):
    A, B = map(int, input().split())
    priority[B] += 1
    reduce[A].append(B)

for i in range(1, len(priority)):
    if priority[i] == 0:
        h.heappush(heap, i)

while heap:
    num = h.heappop(heap)

    if reduce[num]:
        for i in reduce[num]:
            priority[i] -= 1

            if priority[i] == 0:
                h.heappush(heap, i)

    print(num, end=" ")
