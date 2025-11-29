N = int(input())
s = set(map(int, input().split()))
M = int(input())
c = list(map(int, input().split()))

for i in c:
    if i in s:
        print(1, end=" ")
    else:
        print(0, end=" ")
