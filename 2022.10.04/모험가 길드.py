n = int(input())
adventures = list(map(int,input().split()))
adventures.sort()
adventrues_count = 0
result = 0

for i in range(n):
    adventrues_count += 1
    if adventures[i] <= adventrues_count:
        result += 1
        adventrues_count = 0

print(result)

