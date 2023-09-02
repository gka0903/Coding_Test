def spiralOrder(matrix):
    right = len(matrix[0])
    bottom = len(matrix)
    x = 0
    y = 0
    direction = 1
    answer = [matrix[0][0]]
    matrix_b = [[True] * bottom for _ in range(bottom)]
    matrix_b[0][0] = False
    while direction != 6:
        print(direction)
        if direction % 4 == 1:
            print(x, y, right)
            for _ in range(right):
                if x < right - 1:
                    x += 1
                else:
                    break
                if matrix_b[y][x]:
                    answer.append(matrix[y][x])
                    matrix_b[y][x] = False
                else:
                    x -= 1
                    break
        elif direction % 4 == 2:
            for _ in range(bottom):
                if y < bottom - 1:
                    y += 1
                else:
                    break
                if matrix_b[y][x]:
                    answer.append(matrix[y][x])
                    matrix_b[y][x] = False
                else:
                    x -= 1
                    break
        elif direction % 4 == 3:
            for _ in range(x, 0, -1):
                if x > 0:
                    x -= 1
                else:
                    break
                if matrix_b[y][x]:
                    answer.append(matrix[y][x])
                    matrix_b[y][x] = False
                else:
                    x -= 1
                    break
        else:
            for _ in range(y, 0, -1):
                if y > 0:
                    y -= 1
                else:
                    break
                if matrix_b[y][x]:
                    answer.append(matrix[y][x])
                    matrix_b[y][x] = False
                else:
                    y -= 1
                    break
        direction += 1
        print(matrix_b)
    return answer


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
