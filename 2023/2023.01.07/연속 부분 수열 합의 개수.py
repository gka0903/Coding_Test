def solution(elements):
    answer = 0
    arr = []
    for index in range(len(elements)):
        for i in range(1, len(elements) + 1):
            if index + i < len(elements):
                check = sum(elements[index: index + i])
                if check not in arr:
                    arr.append(check)
    return sorted(arr), len(arr)


print(solution([7, 9, 1, 1, 4]))
