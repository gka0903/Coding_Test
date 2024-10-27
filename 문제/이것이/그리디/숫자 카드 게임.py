# M N 행렬
# 가장 높은 카드 뽑기
# 조건 : 뽑을 행을 선택 후 가장 낮은 카드를 뽑아야 함

def solution():
    n, m = map(int, input("행과 열의 수를 입력하세요: ").split())
    matrix = []

    print("행렬 값을 입력하세요:")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = 0
    for row in matrix:
        min = 100
        for num in row:
            if num < min:
                min = num

        if result < min:
            result = min

    return result


print(solution())
