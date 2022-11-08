n = int(input())
adventures = list(map(int, input().split()))
adventures.sort()
adventures_count = 0
result = 0

for i in range(n):
    adventures_count += 1
    if adventures[i] <= adventures_count:
        result += 1
        adventures_count = 0

print(result)

