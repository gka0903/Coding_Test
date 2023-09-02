def solution(s):
    answer = 0
    check = s[0]
    same_num = 0
    dif_num = 0
    for i in range(len(s)):
        if s[i] == check:
            same_num += 1
        else:
            dif_num += 1

        if same_num == dif_num:
            same_num = 0
            dif_num = 0
            answer += 1
            if i + 1 < len(s):
                check = s[i + 1]
        print(same_num, dif_num, s[i], answer)
    if same_num != 0 or dif_num != 0:
        answer += 1

    return answer


print(solution("aaabbaccccabba"))
