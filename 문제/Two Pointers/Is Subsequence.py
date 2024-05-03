def solution(s, t):
    ps = 0
    if s == "":
        return True
    for i in range(len(t)):
        if t[i] == s[ps]:
            ps += 1
            if ps >= len(s):
                return True

    return False


print(solution("abc", "ahbgdc"))
print(solution("axc", "ahbgdc"))
