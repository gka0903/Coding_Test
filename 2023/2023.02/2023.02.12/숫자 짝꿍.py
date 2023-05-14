def solution(X, Y):
    answer = ''
    arr_x = [0] * 10
    arr_y = [0] * 10
    for i in X:
        arr_x[int(i)] += 1
    for i in Y:
        arr_y[int(i)] += 1
    for num in range(9, -1, -1):
        m = min(arr_x[num], arr_y[num])
        answer += str(num) * m
    if len(answer) == 0:
        return '-01'
    if answer[0] == '0':
        return '0'
    return answer


print(solution("100", "123450"))
