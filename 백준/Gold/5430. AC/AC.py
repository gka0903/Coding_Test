import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    command = input()
    n = int(input())
    raw_string = input().rstrip()
    is_error = False
    is_flip = False

    if n == 0:
        target_list = []
    else:
        target_list = list(map(int, raw_string[1:-1].split(",")))

    target = deque(target_list)

    for c in command:
        if c == "R":
            is_flip = not is_flip
        if c == "D":
            if len(target) < 1:
                is_error = True
                break

            if is_flip:
                target.pop()
            else:
                target.popleft()

    if is_error:
        print("error")
        continue

    if is_flip:
        target.reverse()

    print("[" + ",".join(list(map(str, target))) + "]")
