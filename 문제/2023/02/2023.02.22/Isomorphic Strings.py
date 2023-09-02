def isIsomorphic(s, t):
    dic = {}
    dic2 = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = t[i]
        else:
            if dic[s[i]] != t[i]:
                return False
        if t[i] not in dic2:
            dic2[t[i]] = s[i]
        else:
            if dic2[t[i]] != s[i]:
                return False
    return True


print(isIsomorphic("bbbaaaba", "aaabbbba"))
