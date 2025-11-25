import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

for target in B:
    s = 0
    e = len(A) - 1

    check = True
    while s <= e:
        mid = (s + e) // 2
        if A[mid] == target:
            print(1)
            check = False
            break
        elif A[mid] > target:
            e = mid - 1
        else:
            s = mid + 1

    if check:
        print(0)
