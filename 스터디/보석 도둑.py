import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
h = heapq
jewel = []
backpack = []

for i in range(N):
    m, v = map(int, input().split())
    h.heappush(jewel, (m, v))

for i in range(K):
    w = int(input())
    h.heappush(backpack, w)

result = 0
able_backpack = []

while backpack:
    b = h.heappop(backpack)

    while jewel and b >= jewel[0][0]:
        mass, value = h.heappop(jewel)
        h.heappush(able_backpack, (-value, mass))

    if able_backpack:
        result += -h.heappop(able_backpack)[0]


print(result)
