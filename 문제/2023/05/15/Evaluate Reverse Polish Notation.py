def solution(tokens):
    stack = []
    for i in tokens:
        if i == '+' or i == '-' or i == '*' or i == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(int(eval(str(a) + i + str(b))))
        else:
            stack.append(i)

    return stack[-1]


print(solution(["4", "13", "5", "/", "+"]))
