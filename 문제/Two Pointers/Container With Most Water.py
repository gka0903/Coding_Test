def solution(height):
    point_one = 0
    point_two = len(height) - 1
    res = 0
    while point_one < point_two:
        w = (point_two - point_one) * min(height[point_one], height[point_two])
        if w >= res:
            res = w
        if height[point_one] > height[point_two]:
            point_two -= 1
        else:
            point_one += 1

    return res


print(solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
