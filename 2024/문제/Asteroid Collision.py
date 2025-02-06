def solution(asteroid):
    left = 0
    right = len(asteroid) - 1
    index = -1

    asteroid.sort()
    while left <= right:

        mid = (left + right) // 2
        if asteroid[mid] > 0:
            right = mid - 1
            index = right
        else:
            left = mid + 1

    index

    return result


print(solution([5, 10, -5]))
