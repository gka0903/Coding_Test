while True:
    check = True
    s = input()

    if s == '.':
        break

    stack = []
    for w in s:
        if w == '(' or w == '[':
            stack.append(w)

        if w == ']' or w == ')':
            if not stack:
                check = False
                break

            p = stack.pop()
            if w == ']' and p == '(':
                check = False
                break

            if w == ')' and p == '[':
                check = False
                break

    if stack:
        check = False

    if check:
        print("yes")
    else:
        print("no")
