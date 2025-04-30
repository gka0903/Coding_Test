# 500 100 50 10 무제한
# 최소 동전

def solution(money):
    coins = [500, 100, 50, 10]
    count = 0

    for coin in coins:
        count += money // coin
        money %= coin

    return count


print(solution(1760))
