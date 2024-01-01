def solution(emergency):
    answer = []
    arr = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(arr.index(i) + 1)
    return answer


print(solution([3, 76, 24]))
