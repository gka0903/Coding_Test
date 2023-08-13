def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split('=')
        result = eval(i[0])
        if result == int(i[1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))