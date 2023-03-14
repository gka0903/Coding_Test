import sys

a, b = map(int, sys.stdin.readline().split())

count = 0
arr = [1] * a
while len(arr) > b:
    if len(arr) % 2 == 0:
        arr = [arr[0]] * (len(arr) // 2)
    else:
        if arr[-1] == 1:
            count += 1
            arr = [arr[0]] * ((len(arr) + 1) // 2)
        # else:
        #     if arr[-1] % 2 == 0:

print(arr)
print(count)
