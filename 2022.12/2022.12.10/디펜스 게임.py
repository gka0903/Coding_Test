def solution(n, k, enemy):
    start = 0
    end = len(enemy)
    while start <= end:
        mid = (start + end) // 2
        arr = enemy[0:mid+1]
        arr.sort(reverse=True)
        if sum(arr[k:]) == n:
            return mid + 1
        elif sum(arr[k:]) > n:
            end = mid - 1
        else:
            start = mid + 1

    if mid == len(enemy):
        return mid
    return mid + 1




print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
