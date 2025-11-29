# 입력
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
cases = []

for _ in range(N):
    n = int(input())
    c = list(map(int, sys.stdin.readline().split()))
    cases.append(c)

# results = []
results = []

# cases 반복문
for case in cases:
    # result = 0
    result = 0

    # 나 혼자 -> set
    alone = set()
    for i in case:
        #  학생들 index로 보기 쉽게
        case[i] -= 1

        if case == i:
            alone.add(i)

    # network list
    net = [-1] * (len(case))

    # visit
    visit = [False] * len(case)


    def dfs(cur, index):
        global net

        if not visit[cur]:
            net[index] = cur
            return

        visit[cur] = True
        dfs(case[cur], index)


    # 반복문 학생들
    for i in range(len(case)):
        # dfs(s) 현재 학생 매개 변수
        dfs(i, i)

        # dict
        d = defaultdict(list)

        # dict에 같은 부모를 가진 학생들 모으기
        for i in range(len(net)):
            d[i].append(net[i])

        # 혼자 팀 돌면서 dict 확인
        # 혼자 팀에 속해 있으면 + 1 없으면 len
        # results에 값 추가
        for i in alone:
            for k, v in d.items():
                if i in v:
                    result += 1
                else:
                    result += len(v)

    results.append(result)

print(results)
