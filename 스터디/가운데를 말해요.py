import heapq
import sys

h = heapq
input = sys.stdin.readline

N = int(input())
left = []
right = []
left_cnt = 0
right_cnt = 0

for i in range(N):
    n = int(input())

    if left_cnt != right_cnt:
        h.heappush(right, n)
        right_cnt += 1
    else:
        n = -n
        h.heappush(left, n)
        left_cnt += 1

    if right and -left[0] > right[0]:
        l = -h.heappop(left)
        r = h.heappop(right)

        h.heappush(left, -r)
        h.heappush(right, l)

    print(-left[0])
