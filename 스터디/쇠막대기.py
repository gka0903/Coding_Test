import sys

input = sys.stdin.readline
s = input().strip()
stack = []
result = 0

for i, p in enumerate(s):
    if p == '(':

        # 새로운 막대기 등장
        result += 1
        stack.append((i, p))
    else:
        prev_i, prev_p = stack.pop()

        # 레이저라면
        # 현재 막대기 수 만큼 더 하기(잘리면 +1)
        # 레이저는 막대기가 아니니까 -1
        if prev_i == i - 1:
            result -= 1
            result += len(stack)

print(result)
