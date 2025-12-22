import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    num = int(input())
    rooms = [False] * (num + 1)

    for i in range(1, num + 1):
        for j in range(i, num + 1, i):
            rooms[j] = not rooms[j]

    result = 0

    for i in range(1, num + 1):
        if rooms[i]:
            result += 1

    print(result)
