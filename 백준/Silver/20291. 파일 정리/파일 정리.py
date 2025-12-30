import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
h = heapq
n = int(input())
file_count = defaultdict(int)
file_ = []

for i in range(n):
    s = input().strip()
    file_name, extension = s.split(".")

    if extension not in file_count:
        h.heappush(file_, extension)

    file_count[extension] += 1

while file_:
    cur_file = h.heappop(file_)
    print(cur_file, file_count[cur_file])
