n = int(input())
homeworks = []

for i in range(n):
    d, w = list(map(int, input().split()))
    homeworks.append((d, w))

last_day = max(homeworks)
homeworks.sort(reverse=True, key=lambda x: x[1])
sum = 0

for i in range(last_day[0], 0, -1):
    max_score = 0
    for j in homeworks:
        if j[0] >= i:
            sum += j[1]
            homeworks.remove(j)
            break

print(sum)

# 7
# 4 60
# 4 40
# 1 20
# 2 50
# 3 30
# 4 10
# 6 5
