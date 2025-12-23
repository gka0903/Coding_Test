import sys

input = sys.stdin.readline
N, M = map(int, input().split())
baskets = [i for i in range(N + 1)]


for _ in range(M):
    i, j, k = map(int, input().split())
    left = baskets[i:k]
    right = baskets[k : j + 1]
    baskets[i : j + 1] = right + left

print(*baskets[1:])
