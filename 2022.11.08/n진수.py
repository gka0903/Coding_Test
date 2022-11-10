import queue
from collections import deque


def convert(n, number):
    if n == 2:
        return format(number, 'b')
    elif n == 16:
        return format(number, 'x')


def solution(n, t, m, p):

    return 0


print(solution(2, 4, 2, 1))
print(type(format(30, 'b')))
print(format(30, 'x'))
