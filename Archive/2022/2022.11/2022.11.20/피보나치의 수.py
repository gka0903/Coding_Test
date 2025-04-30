def solution(n):
    answer = 0
    cash = [0] * 10001
    cash[1], cash[2] = 1, 1
    for i in range(3, n + 1):
        cash[i] = (cash[i - 1] + cash[i - 2]) % 1234567
    answer = cash[n]
    return answer


print(solution(6))
