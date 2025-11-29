import sys

# 입력 받기
N = int(sys.stdin.readline())

# 초기화 set
col, dia_p, dia_m = set(), set(), set()

# 결과값
result = 0


# dfs
# 매개 변수 row 받아서 몇 번 째 줄인지 확인
def dfs(r):
    global result

    # 종료 조건 r == N
    # result += 1 return
    if r == N:
        result += 1
        return

    # 반복 -> 가능 하면 재귀 호출
    for i in range(N):
        d_p = r - i
        d_m = r + i

        if i not in col and d_p not in dia_p and d_m not in dia_m:
            col.add(i)
            dia_p.add(d_p)
            dia_m.add(d_m)
            dfs(r + 1)
            col.remove(i)
            dia_p.remove(d_p)
            dia_m.remove(d_m)


dfs(0)

# 결과 출력
print(result)
