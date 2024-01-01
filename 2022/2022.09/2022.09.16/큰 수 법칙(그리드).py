n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers = sorted(numbers, reverse = True)
num_first = numbers[0]
num_second = numbers[1]

answer = 0

while True:
	for i in range(k):
		if m == 0:
			break
		answer += num_first
		m -= 1
	if m == 0 :
		break
	answer += num_second
	m -= 1

print(answer)