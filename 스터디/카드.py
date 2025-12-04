N = int(input())
c = {}
m = 0
result = 0

for i in range(N):
    n = int(input())

    if n in c:
        c[n] += 1
    else:
        c[n] = 1

    if m < c[n]:
        m = c[n]
        result = n
    elif m == c[n]:
        if result > n:
            result = n

print(result)
