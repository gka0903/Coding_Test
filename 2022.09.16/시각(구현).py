h = int(input())
answer = 0
sum = 0

for i in range(h + 1):
	for j in range(60):
		for k in range(60):
			if "3" in str(i) + str(j) + str(k):
				answer += 1
			sum += 1

print(answer)
print(sum)