def solution(N, stages):
    arr = []
    answer = []
    check = []
    for stage in range(1, N + 1):
        player = 0
        player_fail = 0
        for player_stage in stages:
            if stage < player_stage:
                player += 1
            elif stage == player_stage:
                player_fail += 1
                player += 1
        if player == 0:
            arr.append(0)
        else:
            arr.append(float(player_fail / player))
    for i, j in enumerate(arr):
        check.append([j, i + 1])
    arr.sort(reverse=True)
    for num in arr:
        for index in range(len(check)):
            if num == check[index][0]:
                answer.append(check[index][1])
                check.pop(index)
                break
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
