# 숫자 배열 주어짐
# n의 길이 배열
# M만큼 더해서 가장 큰 수
# 조건 : K만큼의 반복만 허용됨

def solution():
    n, m, k = map(int, input("n, m, k를 입력하세요: ").split(' '))
    arr = list(map(int, input("숫자를 입력하세요: ").split(' ')))

    # arr 정렬
    arr.sort(reverse=True)

    result = 0

    # M만큼 반복
    # count > k이면 두번째 수
    count = 0
    for i in range(m):
        count += 1
        if count > k:
            result += arr[1]
            count = 0
            continue

        result += arr[0]
        print(result)

    return result


print(solution())
