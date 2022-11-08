numbers = input()
count = 0
for i in range(1, len(numbers)):
    num = int(numbers[i])
    if numbers[i - 1] != numbers[i]:
        count += 1

if count % 2 == 0:
    result = count // 2
else:
    result = (count + 1) // 2

print(result)