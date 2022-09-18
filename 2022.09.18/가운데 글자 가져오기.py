def solution(s):
    answer = ''
    l = len(s)
    result_l = l // 2
    if l % 2 != 0: answer = s[result_l]
    else: answer = s[result_l - 1 : result_l + 1]
                   
    return answer

print(solution("ab*de"))
print(solution("qwer"))