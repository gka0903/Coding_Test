import sys

input = sys.stdin.readline
s = input().strip()
stack = []
cal = []
result = 0

for i, p in enumerate(s):
    if p == '(' or p == '[':
        stack.append((i, p))
    else:
        if not stack:
            result = 0
            cal = []
            break

        prev_i, prev_p = stack.pop()

        if (p == ')' and prev_p == '[') or (p == ']' and prev_p == '('):
            result = 0
            cal = []
            break

        if prev_i == i - 1:
            if prev_p == '(':
                cal.append((prev_i, 2))
            if prev_p == '[':
                cal.append((prev_i, 3))
        else:
            p_s = 0

            while cal:
                if cal[-1][0] < prev_i:
                    break

                p_i, p_p = cal.pop()
                p_s += p_p

            if prev_p == '(':
                cal.append((prev_i, p_s * 2))
            if prev_p == '[':
                cal.append((prev_i, p_s * 3))

if stack:
    cal = []
    result = 0

for i, n in cal:
    result += n

print(result)
