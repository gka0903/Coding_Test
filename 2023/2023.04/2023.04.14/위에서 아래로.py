n = int(input())
arr = []
for i in range(n):
    number = int(input())
    arr.append(number)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
