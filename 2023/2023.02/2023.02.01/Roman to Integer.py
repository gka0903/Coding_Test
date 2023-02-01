def romanToInt(s):
    answer = 0
    prev = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s) - 1, -1, - 1):
        if dic[s[i]] <= prev:
            answer -= dic[s[i]]
        else:
            answer += dic[s[i]]
        prev = dic[s[i]]
    return answer


print(romanToInt("MCMXCIV"))
