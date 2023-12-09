def solution(s):
    p1 = 0
    p2 = 0
    check_string = set()
    result = 0
    while p1 < len(s) and p2 < len(s):
        if s[p2] not in check_string:
            check_string.add(s[p2])
            p2 += 1
        else:
            check_string.remove(s[p1])
            p1 += 1
        result = max(result, len(check_string))

    return result


print(solution("abcabcbb"))
