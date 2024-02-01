def solution(matrix):
    result = float('inf')
    for i in range(3):
        # 1 2 3
        for j in range(1, 4):
            check = 0
            for num in matrix[i]:
                check += abs(num - j)
            result = min(result, check)

        for j in range(1, 4):
            check = 0
            for num in [matrix[0][i], matrix[1][i], matrix[2][i]]:
                check += abs(num - j)
            result = min(result, check)

    return result


print(solution([[1, 2, 3], [1, 1, 2], [2, 1, 3]]))
