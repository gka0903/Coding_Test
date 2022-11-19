def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if count % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        count += 1
        if s[i] == " ":
            count = 0

    return answer


print(solution("try hello world"))
print(solution("IM Your Father"))
