def solution(s):
    answer = True
    s = list(s)
    for i in range(len(s)):
        if s[i] == "(":
            answer = False
            for j in range(i, len(s)):
                if s[j] == ")":
                    s[j] = " "
                    answer = True
                    break
    for i in s:
        if i == ")":
            answer = False
    
    return answer

print(solution("(()("))