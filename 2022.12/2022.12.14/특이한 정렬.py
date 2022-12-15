def solution(numlist, n):
    answer = []
    arr = list(map(lambda x: abs(x - n), numlist))
    result = []
    for i in range(len(numlist)):
        result.append([arr[i], numlist[i]])
    result.sort()
    for j in range(1, len(result)):
        if result[j][0] == result[j - 1][0] and result[j][1] > result[j - 1][1]:
            result[j], result[j - 1] = result[j - 1], result[j]
    for i in result:
        answer.append(i[1])
    return answer


print(solution([1, 2, 3, 4, 5, 6], 4))
