def solution(n):
    cash = [1, 2]
    for i in range(2, n):
        cash.append(cash[i - 1] + cash[i - 2])
    print(cash)
    return cash[n - 1] % 1234567



print(solution(100))
