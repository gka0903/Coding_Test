import sys

input = sys.stdin.readline
s = input().strip()

stack = []

for c in s:
    stack.append(c)

    while "".join(stack[-4:]) == "PPAP":
        for _ in range(3):
            stack.pop()


if stack == ["P"]:
    print("PPAP")
else:
    print("NP")
