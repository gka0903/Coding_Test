def solution(land):
    answer = 0
    pre_index = -1

    for i in range(len(land)):
        m = 0
        cur_index = 0
        for j in range(len(land[i])):
            if land[i][j] > m:
                if pre_index != j:
                    cur_index = j
                    m = land[i][j]

        pre_index = cur_index
        answer += land[i][cur_index]

    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
