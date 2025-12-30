import sys

input = sys.stdin.readline
n = int(input())
numbers = []

for _ in range(n):
    s = input().strip()
    number = ""
    is_alpha = True

    for c in s:
        if ord("a") <= ord(c) <= ord("z"):
            if is_alpha:
                continue
            else:
                is_alpha = True
                numbers.append(number)
                number = ""
        else:
            if is_alpha:
                is_alpha = False

            number += c

    if not is_alpha and number != "":
        numbers.append(number)

numbers = list(map(int, numbers))
numbers.sort()

for n in numbers:
    print(n)
