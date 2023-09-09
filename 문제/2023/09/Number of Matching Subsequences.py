def solution(s, words):
    result = 0
    results = {}
    for word in words:
        index = 0
        check = len(word)
        if word in results:
            result += 1
            pass
        for char in s:
            if check == 0:
                break
            if word[index] == char:
                index += 1
                check -= 1
        if check == 0:
            results.get(word)
            result += 1
    return result


print(solution("abcde", ["a", "bb", "acd", "ace"]))
