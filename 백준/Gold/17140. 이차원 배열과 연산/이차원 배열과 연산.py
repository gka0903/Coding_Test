import sys
from collections import Counter

input = sys.stdin.readline


def sorting(li):
    c = Counter(li)
    l = []

    for key, value in c.items():
        if key != 0:
            l.append((value, key))

    l.sort()
    sorted_l = []

    for cnt, number in l:
        sorted_l.append(number)
        sorted_l.append(cnt)

    return sorted_l


def padding(matrix, size):
    new_matrix = []

    for l in matrix:
        while len(l) < size:
            l.append(0)

        new_matrix.append(l)

    return new_matrix


def R_oper(matrix):
    max_len = 0
    new_matrix = []

    for l in matrix:
        sorted_l = sorting(l)

        if len(sorted_l) > 100:
            sorted_l = sorted_l[:100]

        new_matrix.append(sorted_l)

        if len(sorted_l) > max_len:
            max_len = len(sorted_l)

    return new_matrix, max_len


r, c, k = map(int, input().split())
A = []
time = 0

for i in range(3):
    A.append(list(map(int, input().split())))

while time <= 100:
    if r - 1 < len(A) and c - 1 < len(A[0]):
        if A[r - 1][c - 1] == k:
            break

    row_cnt = len(A)
    column_cnt = len(A[0])

    # R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
    # C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
    if row_cnt >= column_cnt:
        A, max_len = R_oper(A)
        A = padding(A, max_len)
    else:
        A = list(map(list, zip(*A)))
        A, max_len = R_oper(A)
        A = padding(A, max_len)
        A = list(map(list, zip(*A)))

    time += 1

if time > 100:
    print(-1)
else:
    print(time)
