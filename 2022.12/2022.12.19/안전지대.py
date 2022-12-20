def solution(board):
    answer = 0
    n = len(board)
    boom = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    stack = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                stack.append([i, j])

    for i in stack:
        for bang in boom:
            x = i[0] + bang[0]
            y = i[1] + bang[1]
            if n - 1 >= x >= 0 and n - 1 >= y >= 0:
                board[i[0] + bang[0]][i[1] + bang[1]] = 1

    for i in board:
        answer += i.count(0)

    return answer


print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
