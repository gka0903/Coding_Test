def solution(brown, yellow):
    answer = []
    y = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y.append(i)
    for j in range(len(y)):
        if ((y[j] * 2) + (y[-1 - j] * 2) + 4) == brown:
            answer = [y[j] + 2, y[-1 - j] + 2]
    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer



print(solution(24, 24))
