def solution(array):
    answer = 0
    array = list(map(str, array))
    array = "".join(array)
    for i in array:
        if i == '7':
            answer += 1

    return answer


print(solution([7, 77, 17]))
