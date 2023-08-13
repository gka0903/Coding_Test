def solution(wallpaper):
    a = len(wallpaper)
    x1, y1, x2, y2 = a, a, 0, 0
    for i in range(a):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x1 = min(x1, j)
                y1 = min(y1, i)
                x2 = max(x2, j + 1)
                y2 = max(y2, i + 1)
    return [y1, x1, y2, x2]


print(solution(["..", "#."]))
