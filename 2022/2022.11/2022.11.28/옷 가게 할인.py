def solution(price):
    if price < 100000:
        return price
    elif price < 300000:
        return price - (price // 20)
    elif price < 500000:
        return price - (price // 10)
    else:
        return price - (price // 5)


print(solution(1000000))
