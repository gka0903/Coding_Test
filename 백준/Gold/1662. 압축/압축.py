import sys

input = sys.stdin.readline
stack = []
s = input().strip()

for i in range(len(s)):
    if s[i] == ")":
        num = 0
        left_index = 0

        while True:
            idx, number = stack.pop()

            if number == -1:
                left_index = idx
                break

            num += number

        stack.pop()
        stack.append([i, int(s[left_index - 1]) * num])
    else:
        if s[i] == "(":
            stack.append([i, -1])
        else:
            stack.append([i, 1])

result = 0

while stack:
    result += stack.pop()[1]

print(result)
