import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
C = int(input())

# n + 1은 사용 하지 않는 0번 인덱스를 포함 하기 때문
visit = [False] * (N + 1)
dic = defaultdict(list)

# 반복으로 dic 만들어주기
for i in range(C):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)


def dfs(c, d):
    visit[c] = True

    for com in d[c]:
        if not visit[com]:
            dfs(com, d)


dfs(1, dic)

print(sum(visit))
