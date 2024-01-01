def solution(arr):
    result = 0
    s = 0
    end = 0
    for start in range(len(arr)):
        while s < len(arr) and end < len(arr):
            s += arr[end]
            end += 1
        if s == len(arr):
            result += 1
        s -= arr[start]
        print(start, end, s)
    return result


print(solution([1, 2, 3, 2, 5]))
