def solution(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            if i > 0:
                flowerbed[i - 1] = -1
            if i < len(flowerbed) - 1:
                flowerbed[i + 1] = -1
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            if i < len(flowerbed) - 1:
                flowerbed[i + 1] = -1
            n -= 1
    if n <= 0:
        return True
    return False


print(solution([1, 0, 0, 0, 0, 0, 1], 2))
