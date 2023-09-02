def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for index, current_temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < current_temperature:
            target = stack.pop()
            answer[target] = index - target
        stack.append(index)

    return answer


print(dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
