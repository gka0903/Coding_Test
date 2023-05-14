def solution(s):
    length_s = len(s)
    result = length_s
    for i in range(1, length_s // 2 + 1):
        result_string = ""
        a1 = s[0:i]
        count = 1
        for j in range(i, length_s, i):
            if a1 == s[j:j + i]:
                count += 1
            else:
                result_string += str(count) + a1 if count >= 2 else a1
                a1 = s[j:j + i]
                count = 1
        result_string += str(count) + a1 if count >= 2 else a1
        result = min(result, len(result_string))

    return result


print(solution("aabbaccc"))
