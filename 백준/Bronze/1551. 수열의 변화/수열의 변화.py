import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split(",")))
B = []

for _ in range(K):
    B = []
    for i in range(1, N):
        B.append(A[i] - A[i - 1])

    N -= 1
    A = B[:]

print(*A, sep=",")
