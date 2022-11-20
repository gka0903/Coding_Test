print(ord('a'), ord('z'))
print(ord('A'), ord('Z'))


def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += " "
            continue
        num = ord(i) + n
        if ord(i) <= ord('z') < num:
            answer += chr(num + (ord('a') - 1) - ord('z'))
        elif ord(i) <= ord('Z') < num:
            answer += chr(num + (ord('A') - 1) - ord('Z'))
        else:
            answer += chr(num)

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("Z", 1))
print(solution("a B z", 4))
