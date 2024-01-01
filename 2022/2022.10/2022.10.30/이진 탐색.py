# 이진탐색 계속 절반을 나누며 값을 찾는 탐색

def binary(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary(array, target, mid + 1, end)
    else:
        return binary(array, target, start, mid - 1)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary(array, target, 0, n - 1)
if result is None:
    print("원소가 없음")
else:
    print(result + 1)
