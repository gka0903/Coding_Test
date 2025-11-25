import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
birds = []
for i in range(N):
    s = list(input().strip().split(" "))
    q = deque(s)
    birds.append(q)

target = deque(list(input().strip().split(" ")))
c = True
while target:
    t = target.popleft()
    c = False
    for j in birds:
        if j and j[0] == t:
            j.popleft()
            c = True
            break

    if not c:
        break

for b in birds:
    if b:
        c = False

if c:
    print("Possible")
else:
    print("Impossible")
