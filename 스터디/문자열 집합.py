import sys

input = sys.stdin.readline
hashMap = set()
N, M = map(int, input().split())
result = 0

for i in range(N):
    s = input()
    hashMap.add(s)

for j in range(M):
    s = input()
    if s in hashMap:
        result += 1

print(result)
