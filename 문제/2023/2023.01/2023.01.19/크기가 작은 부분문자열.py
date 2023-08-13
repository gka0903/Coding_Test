def solution(t, p):
    arr = []
    for i in range(len(t)):
        if i + len(p) <= len(t):
            arr.append(t[i:i + len(p)])
    return len([num for num in arr if int(num) <= int(p)])


print(solution("3141592", "271"))
