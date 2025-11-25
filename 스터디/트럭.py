import sys
from collections import deque

input = sys.stdin.readline
bridge = deque([])
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
truck = deque(trucks)
time = 0
weight = 0

while truck:
    time += 1

    if bridge and time - bridge[0][1] >= w:
        weight -= bridge[0][0]
        bridge.popleft()

    if weight + truck[0] <= l:
        weight += truck[0]
        bridge.append((truck.popleft(), time))

while bridge:
    time += 1
    if time - bridge[0][1] >= w:
        bridge.popleft()

print(time)
