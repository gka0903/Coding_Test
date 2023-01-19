def solution(need_coke, new_cock, bottle):
    answer = 0
    while bottle >= need_coke:
        count = bottle // need_coke
        count_last = bottle % need_coke
        get_coke = count * new_cock

        bottle = get_coke + count_last
        answer += get_coke

    return answer


print(solution(4, 2, 20))
