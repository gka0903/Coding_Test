a = int(input())
sum = 0

for i in range(a + 1):
    for j in range(60):
        for z in range(60):
            if '3' in str(i) + str(j) + str(z):
                sum += 1

print(sum)