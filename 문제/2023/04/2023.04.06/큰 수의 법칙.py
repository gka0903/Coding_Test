n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
count = k
answer = 0
while m > 0:
    if count == 0:
        count = k
        answer += data[-2]
    else:
        count -= 1
        answer += data[-1]
    m -= 1
print(answer)
