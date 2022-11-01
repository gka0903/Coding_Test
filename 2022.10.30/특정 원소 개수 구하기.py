from bisect import bisect_right, bisect_left

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

left = bisect_left(array, x)
right = bisect_right(array, x)

print(right - left)
