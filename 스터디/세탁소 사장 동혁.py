import sys

input = sys.stdin.readline
N = int(input())
coins = [25, 10, 5, 1]

for i in range(N):
    num = int(input())
    result = [0] * len(coins)
    for i in range(len(coins)):
        if num >= coins[i]:
            result[i] = num // coins[i]
            num = num - (coins[i] * (num // coins[i]))
        elif num % coins[i] == 0:
            result[i] = num // coins[i]
            break

    print(*result)
