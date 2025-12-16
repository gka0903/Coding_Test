import sys

input = sys.stdin.readline
N = int(input())
empty_table = [0] * N
up_table = [0] * N
down_table = [0] * N
empty_table[0] = 1
up_table[0] = 1
down_table[0] = 1

for i in range(1, N):
    empty_table[i] = (up_table[i - 1] + down_table[i - 1] + empty_table[i - 1]) % 9901
    up_table[i] = (down_table[i - 1] + empty_table[i - 1]) % 9901
    down_table[i] = (up_table[i - 1] + empty_table[i - 1]) % 9901

print((empty_table[-1] + up_table[-1] + down_table[-1]) % 9901)
