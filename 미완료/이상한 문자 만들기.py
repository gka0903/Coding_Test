def solution(s):
    answer = ''
    s = s.split()

    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else: 
                answer += i[j]
        if i != s[len(s) - 1]:
            answer += " "

    return answer

print(solution("try hello world"))
print(solution(" my favorit food is kimchi "))