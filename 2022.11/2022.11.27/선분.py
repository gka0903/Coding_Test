def solution(lines):
    answer = 0
    lines.sort()
    for i in range(lines[0][0], lines[-1][1] + 1):
        count = 0
        for j in lines:
            if j[0] <= i and i + 1 <= j[1]:
                count += 1
        if count >= 2:
            answer += 1

    return answer


print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))
