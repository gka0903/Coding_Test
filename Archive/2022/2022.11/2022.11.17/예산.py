def solution(d, budget):
    answer = 0
    d.sort()

    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
        else:
            break

    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
