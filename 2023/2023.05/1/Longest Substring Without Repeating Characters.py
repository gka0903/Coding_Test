def solution(s):
    s = list(s)
    print(s)
    count = 0
    arr = []
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1:
            count += 1
        else:
            arr.append(count)
            count = 0
    arr.append(count)
    m = max(arr)
    if m != 0:
        return m + 1
    else:
        return 0


print(solution("abcabcbb"))
