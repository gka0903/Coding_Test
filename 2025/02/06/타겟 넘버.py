def dfs(numbers, current, index, target):
    if index == len(numbers):
        return 1 if current == target else 0

    next_index = index + 1

    left = dfs(numbers, current + numbers[index], next_index, target)
    right = dfs(numbers, current - numbers[index], next_index, target)

    return left + right


def solution(numbers, target):
    return dfs(numbers, 0, 0, target)


print(solution([1, 1, 1, 1, 1], 3))
