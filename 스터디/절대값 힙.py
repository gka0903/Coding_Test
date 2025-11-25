import heapq
import sys

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    command = int(input())
    if command == 0:
        if arr:
            num1, num = heapq.heappop(arr)
            print(num)
        else:
            print(0)
    else:
        if command < 0:
            heapq.heappush(arr, (-command, command))
        else:
            heapq.heappush(arr, (command, command))
