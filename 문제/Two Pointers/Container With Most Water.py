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


def solution2(height):
    p1 = 0
    p2 = len(height) - 1
    result = 0
    while p2 > p1:
        h = height[p1] if height[p1] < height[p2] else height[p2]
        w = p2 - p1
        if result < h * w:
            result = w * h
        if height[p1] > height[p2]:
            p2 -= 1
        else:
            p1 += 1
    return result


print(solution2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
