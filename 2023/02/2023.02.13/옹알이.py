def solution(babbling):
    answer = 0
    for i in babbling:
        check = ''
        double_check = []
        can_babbling = ["aya", "ye", "woo", "ma"]
        for j in i:
            check += j
            if check in can_babbling:
                if double_check and check == double_check[-1]:
                    break
                double_check.append(check)
                check = ''
        if check == '':
            answer += 1
    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
