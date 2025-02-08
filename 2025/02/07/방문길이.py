def solution(dirs):
    move = {"U": (1, 0), "D": (-1, 0), "L": (0, 1), "R": (0, -1)}
    y, x = 0, 0

    distance = 0
    moved = set()

    for i in dirs:
        dy, dx = move[i]

        ny = y + dy
        nx = x + dx

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if (y, x, ny, nx) not in moved:
                moved.add((y, x, ny, nx))
                moved.add((ny, nx, y, x))
                distance += 1
            y, x = ny, nx

    return distance


print(solution("ULURRDLLU"))
