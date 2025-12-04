n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = A - B

if C:
    print(len(C))
    print(*sorted(C))
else:
    print(0)
