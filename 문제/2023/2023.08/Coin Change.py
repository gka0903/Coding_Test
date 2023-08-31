def solution(coins, amount):
    coins.sort(reverse=True)
    result = 0
    for i in range(len(coins)):
        if amount >= coins[i]:
            count = amount // coins[i]
            amount -= count * coins[i]
            result += count

    if amount != 0:
        return -1
    else:
        return result


print(solution([1, 2, 5], 11))
