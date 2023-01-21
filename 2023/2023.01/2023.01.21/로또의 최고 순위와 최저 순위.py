def solution(lottos, win_nums):
    count = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    intersection = lottos & win_nums
    answer = [len(intersection) + count, len(intersection)]
    for i in range(len(answer)):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
