import sys

n = int(input())
arr = [[0, 0, 0] for i in range(n + 1)]
for i in range(1, n + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[i] = [a, b, c]
for i in range(1, n + 1):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

print(min(arr[-1]))
