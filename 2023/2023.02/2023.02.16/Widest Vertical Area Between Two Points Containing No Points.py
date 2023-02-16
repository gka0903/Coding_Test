def maxWidthOfVerticalArea(points):
    points.sort()
    m = 0
    for i in range(1, len(points)):
        m = max(m, points[i][0] - points[i - 1][0])
    return m


print(maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
