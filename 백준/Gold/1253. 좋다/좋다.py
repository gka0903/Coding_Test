import sys

input = sys.stdin.readline

N = int(input())
numbers_ = list(map(int, input().split()))
numbers_.sort()
result = 0

for i in range(len(numbers_)):
    s = 0
    e = N - 1
    target = numbers_[i]

    if i == 0:
        s = 1

    if i == N - 1:
        e = N - 2

    while s < e:
        sum_ = numbers_[s] + numbers_[e]

        if sum_ == target:
            result += 1
            break
        elif sum_ > numbers_[i]:
            e -= 1

            if e == i:
                e -= 1
        else:
            s += 1

            if s == i:
                s += 1

print(result)
