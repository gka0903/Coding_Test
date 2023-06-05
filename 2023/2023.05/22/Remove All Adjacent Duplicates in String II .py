def solution(s, k):
    while True:
        arr = []
        index = []
        for i in range(len(s)):
            if arr:
                if arr[-1] == s[i]:
                    arr.append(s[i])
                    index.append(i)
                    if len(index) == k:
                        s = s[:index[0]] + s[index[-1] + 1:]
                        print(s)
                        break
                else:
                    arr = [s[i]]
                    index = [i]
                    continue
            else:
                arr.append(s[i])
    return s


print(solution("deeedbbcccbdaa", 3))
