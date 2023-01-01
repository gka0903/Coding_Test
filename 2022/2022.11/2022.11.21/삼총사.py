def solution(number):
    answer = 0
    stack = []
    for i in range(len(number)):
        for j in range(len(number)):
            for z in range(len(number)):
                arr = sorted([i, j, z])
                if number[i] + number[j] + number[z] == 0 and arr not in stack and i != j and j != z and i != z:
                    answer += 1
                    stack.append(arr)
                    print(arr)
    return answer


print(solution([-3, -2, -1, 0, 1, 2, 3]))
