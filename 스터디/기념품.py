from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])
cnt = 0
while len(q) > 1:
    cnt += 1
    t = (cnt ** 3) % len(q) - 1
    target = q[t]

    while True:
        que = q.popleft()
        if que == target:
            break
        q.append(que)

print(q.popleft())
