def solution(numbers):
    arr = [0] * len(numbers)
    answer = []
    stack = []
    for index, current_number in enumerate(numbers):
        while stack and numbers[stack[-1]] < current_number:
            target = stack.pop()
            arr[target] = index - target
        stack.append(index)
    for i in range(len(arr)):
        index = i + arr[i]
        if arr[i] == 0:
            answer.append(-1)
        elif index > len(numbers) - 1:
            answer.append(-1)
        else:
            answer.append(numbers[index])
    return answer


print(solution([2, 3, 3, 5]))
