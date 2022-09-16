n, m = map(int, input().split())
answer = 0

for i in range(n):
	numbers = list(map(int, input().split()))
	min_numbers = min(numbers)
	#max로 min_numbers와 answer값 비교
	answer = max(answer, min_numbers)

print(answer)