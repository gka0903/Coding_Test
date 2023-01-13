import sys

T = int(input())  # Test case
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #', end='')
    print(i + 1, end='')
    print(':', end=' ')
    print(a + b)
