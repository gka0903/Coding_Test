n, m = map(int, input().split())
data = list(map(int, input().split()))
max_data = max(data)


def check(arr, mid):
    count = 0
    for i in arr:
        if i > mid:
            count += i - mid
    return count


def binarySearch(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    result = check(arr, mid)
    if result == target:
        return mid
    elif result > target:
        return binarySearch(arr, target, mid + 1, end)
    else:
        return binarySearch(arr, target, start, mid - 1)


print(binarySearch(data, m, 0, max_data))
