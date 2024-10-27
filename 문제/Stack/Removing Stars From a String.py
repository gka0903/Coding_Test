def solution(s):
    result = []
    for word in s:
        if word == "*":
            result.pop()
            continue
        result.append(word)

    return "".join(result)


print(solution("leet**cod*e"))
