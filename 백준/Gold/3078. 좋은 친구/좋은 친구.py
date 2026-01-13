import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, K = map(int, input().split())
in_k = deque([])
len_dic = defaultdict(int)
result = 0

for i in range(N):
    if len(in_k) > K:
        p_len = in_k.popleft()
        len_dic[p_len] -= 1

    person = input().strip()
    l = len(person)
    result += len_dic[l] if len_dic[l] else 0
    in_k.append(l)
    len_dic[l] += 1

print(result)
