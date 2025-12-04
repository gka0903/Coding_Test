N = int(input())
d = {}

for i in range(N):
    s = input()

    if s in d:
        d[s] += 1
    else:
        d[s] = 1

sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(sorted_d[0][0])
