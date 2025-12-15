S = int(input())
n = 1
result = 0

while S >= n:
    result += 1
    S -= n
    n += 1

print(result)
