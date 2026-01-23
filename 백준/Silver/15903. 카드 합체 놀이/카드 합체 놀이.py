import heapq
import sys

input = sys.stdin.readline
h = heapq
n, m = map(int, input().split())
cards = list(map(int, input().split()))
h.heapify(cards)

for i in range(m):
    A = h.heappop(cards)
    B = h.heappop(cards)

    S = A + B

    h.heappush(cards, S)
    h.heappush(cards, S)

print(sum(cards))
