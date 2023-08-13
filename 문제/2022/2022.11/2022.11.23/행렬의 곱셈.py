def solution(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2[0])

    answer = []
    for i in arr1:
        result = []
        for j in range(arr2_len):
            num = 0
            for z in range(len(i)):
                num += i[z] * arr2[z][j]
            result.append(num)
        answer.append(result)

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
