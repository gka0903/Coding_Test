def solution(height):
    start = 0
    max_water = 0
    end = len(height) - 1
    while start < end:
        w = end - start
        h = height[end] if height[start] > height[end] else height[start]
        max_water = max(max_water, w * h)
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return max_water


print(solution([1, 1]))
