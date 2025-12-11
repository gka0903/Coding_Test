# import bisect
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# wires = []
#
# for i in range(N):
#     A, B = map(int, input().split())
#     wires.append((A, B))
#
# wires.sort()
# lis_arr = [wires[0][1]]
# for i in range(1, N):
#     if lis_arr[-1] < wires[i][1]:
#         lis_arr.append(wires[i][1])
#     else:
#         idx = bisect.bisect_left(lis_arr, wires[i][1])
#         lis_arr[idx] = wires[i][1]
#
# print(N - len(lis_arr))
#
#
import sys

input = sys.stdin.readline

N = int(input())
wires = []

for i in range(N):
    A, B = map(int, input().split())
    wires.append((A, B))

wires.sort()
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
