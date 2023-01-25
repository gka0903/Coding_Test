def maxProfit(prices):
    max_profit = 0
    min_price = 10000
    for i in prices:
        min_price = min(min_price, i)
        max_profit = max(max_profit, min_price - i)
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
