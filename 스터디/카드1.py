from collections import deque

N = int(input())
q = deque([])

for i in range(1, N + 1):
    q.append(i)

while q:
    print(q.popleft(), end=" ")
    if q: q.append(q.popleft())
