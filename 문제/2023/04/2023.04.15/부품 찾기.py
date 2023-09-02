n = int(input())
data = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
data.sort()
check_b = True
print(data)


def binarySearch(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, start, mid - 1, target)
    else:
        return binarySearch(arr, mid + 1, end, target)


for i in check:
    if binarySearch(data, 0, n - 1, i) is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
