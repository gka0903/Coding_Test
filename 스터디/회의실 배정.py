import sys

input = sys.stdin.readline
N = int(input())
meeting = []
for i in range(N):
    meeting.append((list(map(int, input().split()))))

meeting.sort(key=lambda x: (x[1], x[0]))
result = 0
end_time = 0

for s, e in meeting:
    if s >= end_time:
        end_time = e
        result += 1

print(result)
