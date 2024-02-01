def solution(matrix):
    result = float('inf')
    for i in range(3):
        check1 = 0
        check2 = 0
        s1 = sum([matrix[i][0], matrix[i][1], matrix[i][2]])
        s2 = sum([matrix[0][i], matrix[1][i], matrix[2][i]])
        avg1 = s1 // 3
        avg2 = s2 // 3

        for num in matrix[i]:
            check1 += abs(num - avg1)
        result = min(check1, result)

        for num in [matrix[0][i], matrix[1][i], matrix[2][i]]:
            check2 += abs(num - avg2)
        result = min(check2, result)

    return result


print(solution([[1, , 3], [1, 1, 2], [1, 1, 3]]))
