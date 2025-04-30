def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        stack = ''
        print(i)
        for j in i:
            stack += j
            print(stack)
            if stack in baby:
                stack = ''
        if not stack:
            answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
