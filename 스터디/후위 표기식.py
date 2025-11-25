import sys

input = sys.stdin.readline
first = {'*', '/'}
second = {'+', '-'}
third = {'(', ')'}
s = input().strip()

stack = []


def check(c):
    if c in first:
        return 1
    elif c in second:
        return 2
    elif c in third:
        return 3
    return None


for i in s:
    if i not in first and i not in second and i not in third:
        print(i, end="")
    else:
        if i == ')':
            while stack:
                p = stack.pop()
                if p == '(':
                    break
                else:
                    print(p, end="")
        elif i == '(':
            stack.append(i)
        else:
            while stack and check(stack[-1]) <= check(i):
                print(stack.pop(), end="")
            stack.append(i)

while stack:
    print(stack.pop(), end="")
