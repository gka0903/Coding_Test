import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            continue
        else:
            result += 1
print(result)
