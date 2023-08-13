def largestRectangleArea(heights):
    arr = []
    for base in range(1, len(heights) + 1):
        for index in range(0, len(heights)):
            if base == 1:
                height = heights[index]
            else:
                if index + base > len(heights):
                    continue
                for i in heights[index: index + base]:
                    height = min(i, height)
            area = base * height
            arr.append(area)
    return max(arr)


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
