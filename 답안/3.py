def solution(queries):
    answer = []

    # 각 쿼리(n, p)에 대해 형질을 찾아 answer에 추가
    for n, p in queries:
        answer.append(find_trait(n, p))

    return answer


# 재귀적으로 특정 완두콩의 형질을 찾는 함수
def find_trait(n, p):
    # 1. 멈춤 조건: 1세대는 무조건 "Rr"
    if n == 1:
        return "Rr"

    # 2. 부모의 위치 계산
    parent_p = (p - 1) // 4 + 1
    # 부모의 형질을 재귀적으로 찾아옴
    parent_trait = find_trait(n - 1, parent_p)

    # 3. 부모가 순종(RR, rr)이면 자식도 무조건 순종
    if parent_trait != "Rr":
        return parent_trait
    # 4. 부모가 잡종(Rr)이면 자식의 순서에 따라 형질 결정
    else:
        child_order = (p - 1) % 4
        if child_order == 0:
            return "RR"
        elif child_order == 3:
            return "rr"
        else:
            return "Rr"


# --- 테스트를 위한 예제 코드 ---
queries1 = [[3, 5]]
print(f"예제 1 결과: {solution(queries1)}")  # ["RR"]

queries2 = [[3, 8], [2, 2]]
print(f"예제 2 결과: {solution(queries2)}")  # ["rr", "Rr"]

queries3 = [[4, 26]]
print(f"예제 3 결과: {solution(queries3)}")  # ["Rr"]
