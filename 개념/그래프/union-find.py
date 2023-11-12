# 특정 원소가 속한 집합을 찾기
# def find_parent(p, x):
#     if p[x] != x:
#         return find_parent(p, p[x])
#     return x

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


# 두 원소가 속한 집합을 합치기
def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력 및 부모 초기화
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

# # union 연산을 각각 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
# print("각 원소가 속한 집합: ", end="")
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=" ")
#
# print()
#
# # 부모 테이블 내용 출력
# print("부모 테이블: ", end="")
# for i in range(1, v + 1):
#     print(parent[i], end=" ")

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생 O")
else:
    print("사이클 발생 X")
