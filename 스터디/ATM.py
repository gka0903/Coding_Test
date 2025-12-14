import sys

input = sys.stdin.readline
N = int(input())
li = list(map(int, input().split()))
li.sort()
result = 0
time = 0
for t in li:
    time += t
    result += time

print(result)
