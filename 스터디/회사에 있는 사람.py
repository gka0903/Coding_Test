import sys

input = sys.stdin.readline
N = int(input())
s = set()

for i in range(N):
    n, command = input().split()

    if command == "enter":
        s.add(n)
    else:
        s.remove(n)

for i in sorted(s, reverse=True):
    print(i)
