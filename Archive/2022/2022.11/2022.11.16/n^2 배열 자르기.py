def solution(n, left, right):
    answer = []
    for i in range(1, n + 1):
        arr = []
        for j in range(1, n + 1):
            if i >= j:
                arr.append(i)
            else:
                arr.append(j)

        for x in arr:
            answer.append(x)

    print(answer)

    return answer[left:right + 1]


print(solution(3, 2, 5))
