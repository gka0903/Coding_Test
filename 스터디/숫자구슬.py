import sys

input = sys.stdin.readline

N, M = map(int, input().split())
beans = list(map(int, input().split()))
s = max(beans)
e = sum(beans)
target = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 1
    bs = 0

    for i in range(len(beans)):
        if bs + beans[i] > mid:
            bs = 0
            cnt += 1

        bs += beans[i]

    if cnt <= M:
        e = mid - 1
        target = mid
    else:
        s = mid + 1


print(target)
bs = 0
cnt = 0
result = []
for i in range(len(beans)):
    cnt += 1
    bs += beans[i]

    if bs > target:
        result.append(cnt - 1)
        cnt = 1
        bs = beans[i]
    elif (M - len(result) - 1) == (N - i - 1):
        result.append(cnt)
        cnt = 0
        bs = 0


for i in result:
    print(i, end=" ")
