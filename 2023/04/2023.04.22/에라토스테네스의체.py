def solution(n):
    arr = [True for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    result = 0
    for i in range(2, n + 1):
        if arr[i]:
            print(i, end=' ')
            result += 1
    print("\n")
    return result


print(solution(1000))
