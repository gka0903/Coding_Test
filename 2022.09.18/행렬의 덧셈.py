def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        result = list(map(lambda a,b : a + b, arr1[i], arr2[i]))
        answer += [result]

    return answer
    

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
