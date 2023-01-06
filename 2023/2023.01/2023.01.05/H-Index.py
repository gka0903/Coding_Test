def solution(citations):
    arr = []
    for i in range(1000):
        check = 0
        for j in citations:
            if i <= j:
                check += 1
        if check >= i:
            arr.append(i)
    return max(arr)


print(solution([6, 5, 5, 5, 3, 2, 1, 0]))
