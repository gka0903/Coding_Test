import sys

n = input()
arr = []
answer = 0
for i in range(int(n)):
    a, b, c = map(int, sys.stdin.readline().split())
    choose = [a, b, c]
    while True:
        m = min(choose)
        if arr and arr[-1] == choose.index(m):
            choose[choose.index(m)] = 1001
            continue
        else:
            arr.append(choose.index(m))
            break
    print(answer, m)
    answer += m

print(answer)
