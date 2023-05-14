def solution(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = [matrix[0][0]]
    cul_x = [1, 0, -1, 0]
    cul_y = [0, 1, 0, -1]
    check_map = [[False] * n for _ in range(m)]
    check_map[0][0] = True

    def dfs(x, y, count=0):
        nx, ny = x + cul_x[count], y + cul_y[count]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or check_map[ny][nx]:
            nx, ny = x - cul_x[count], y - cul_y[count]
            count += 1
            count %= 4
            dfs(nx, ny, count)
        check_map[ny][nx] = True
        result.append(matrix[ny][nx])
        if len(result) == m * n:
            return result
        print(check_map, y, x)
        return dfs(nx, ny, count)

    return dfs(0, 0)


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
