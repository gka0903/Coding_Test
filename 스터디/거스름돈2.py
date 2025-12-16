import sys

input = sys.stdin.readline
N = int(input())
money = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    if money >= coin:
        if money % coin != 0:
            count = money // coin
            cnt += count
            money -= count * coin
        else:
            cnt += money // coin
            break

print(cnt)
