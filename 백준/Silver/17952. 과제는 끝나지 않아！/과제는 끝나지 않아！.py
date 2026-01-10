import sys

input = sys.stdin.readline

N = int(input())
cur_task = []
stack = []
result = 0

for _ in range(N):
    s = input().strip()

    if s == "0":
        if not cur_task:
            if stack:
                cur_task = stack.pop()

        if cur_task:
            cur_task[1] -= 1

            if cur_task[1] == 0:
                result += cur_task[0]
                cur_task = stack.pop() if stack else []
    else:
        Ne, A, T = map(int, s.split())

        if cur_task:
            stack.append(cur_task)

        cur_task = [A, T - 1]

        if cur_task[1] == 0:
            result += A
            cur_task = stack.pop() if stack else []

print(result)
