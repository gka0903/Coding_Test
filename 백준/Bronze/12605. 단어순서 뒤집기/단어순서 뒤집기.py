import sys

input = sys.stdin.readline
N = int(input())

for i in range(N):
    s = list(input().split())
    new_s = [s[idx] for idx in range(len(s) - 1, -1, -1)]

    print("Case #" + str(i + 1) + ": " + " ".join(new_s))
