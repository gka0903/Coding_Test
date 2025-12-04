import heapq
import sys

input = sys.stdin.readline
h = heapq
T = int(input())

for _ in range(T):
    K = int(input())
    min_q = []
    max_q = []
    s = set()

    for i in range(K):
        command, number = input().split()

        if command == "I":
            h.heappush(min_q, (int(number), i))
            h.heappush(max_q, (-int(number), i))
        elif command == "D":
            n, idx = 0, -1

            if number == "1":
                while max_q:
                    n, idx = h.heappop(max_q)

                    if idx not in s:
                        break
            else:
                while min_q:
                    n, idx = h.heappop(min_q)

                    if idx not in s:
                        break

            if idx != -1:
                s.add(idx)

    while min_q and min_q[0][1] in s:
        h.heappop(min_q)

    while max_q and max_q[0][1] in s:
        h.heappop(max_q)

    if min_q and max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")
