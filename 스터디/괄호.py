T = int(input())

Testing_list = []

for _ in range(T):
    s = input()
    Testing_list.append(s)

for s in Testing_list:
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                stack.append('N')
                break

    if not stack:
        print("YES")
    else:
        print("NO")
