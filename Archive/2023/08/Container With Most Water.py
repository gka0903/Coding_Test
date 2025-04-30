def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        if height[left] > height[right]:
            long_length = height[right]
            width = right - left
            right -= 1
        else:
            long_length = height[left]
            width = right - left
            left += 1
        water = width * long_length
        max_water = max(water, max_water)
    return max_water


print(maxArea([1, 1]))
