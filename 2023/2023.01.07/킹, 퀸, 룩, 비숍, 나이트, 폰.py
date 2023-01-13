arr = list(map(int, input().split()))
correct_arr = [1, 1, 2, 2, 2, 8]
result = []
for i in range(len(correct_arr)):
    check = correct_arr[i] - arr[i]
    result.append(check)

for j in result:
    print(j, end=' ')
