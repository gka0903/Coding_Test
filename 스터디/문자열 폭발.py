import sys

input = sys.stdin.readline
s = input().strip()
boom = input().strip()

stack = []
for i in s:
    stack.append(i)

    if len(stack) >= len(boom):
        if "".join(stack[-len(boom):]) == boom:
            for i in range(len(boom)):
                stack.pop()

result = "".join(stack)

if result == "":
    print("FRULA")
else:
    print(result)
