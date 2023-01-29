def isValid(s):
    arr = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            arr.append(i)
        elif i == ')' and arr and arr[-1] == '(':
            arr.pop()
        elif i == ']' and arr and arr[-1] == '[':
            arr.pop()
        elif i == '}' and arr and arr[-1] == '{':
            arr.pop()
        else:
            return False

    if not arr:
        return True
    else:
        return False


print(isValid("("))
