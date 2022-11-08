numbers = input()
sum = 0

for i in numbers:
    i = int(i)
    if i <= 1 or sum <= 1:
        sum += i
    else:
        sum *= i

print(sum)
