n = int(input())
data = []

for i in range(n):
    input_data = input().split()
    data.append(input_data)

data.sort(key=lambda x: x[1], reverse=True)

for i in data:
    print(i[0], end=' ')
