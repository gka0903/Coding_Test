n = int(input())
K = list(map(int, input().split()))
answer = [K[0]]
for i in range(1, n):
    if i < 2:
        answer.append(max(K[i], K[i - 1]))
    else:
        answer.append(max(answer[i - 1], answer[i - 2] + K[i]))

print(answer[-1])




