import sys

n, k = map(int, sys.stdin.readline().split())
answer = 0
while bin(n)[2::].count('01') > k:
    index = len(bin(n)[2::]) - bin(n)[2::].rfind('01')
    bottle = 2 ** (index - 1)
    answer += bottle
    n += bottle

print(answer)
