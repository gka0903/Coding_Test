import sys

a, b, c = map(int, sys.stdin.readline().split())

print(((a % c) ** (b % c)) % c)
