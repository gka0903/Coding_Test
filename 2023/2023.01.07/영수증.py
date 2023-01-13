x = int(input())
n = int(input())
result = 0
for _ in range(n):
    price, num = input().split()
    result += int(price) * int(num)

if result == x:
    print('Yes')
else:
    print('No')
