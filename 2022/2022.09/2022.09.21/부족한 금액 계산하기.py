def solution(price, money, count):
    sum = 0
    for i in range(1, count + 1):
        sum += price * i
    if money > sum:
        answer = 0
    else:
        answer = sum - money

    return answer

print(solution(3, 20, 4))