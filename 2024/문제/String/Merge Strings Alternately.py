def solution(word1, word2):
    result = ""
    count = len(word1) if len(word1) > len(word2) else len(word2)
    for i in range(count):
        if len(word1) > i:
            result += word1[i]
        if len(word2) > i:
            result += word2[i]
    return result


print(solution("abcd", "pq"))
