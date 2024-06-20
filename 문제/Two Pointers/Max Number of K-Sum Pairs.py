# 문제 array가 주어지고 k가 주어지는데 array의 두 수를 더해서 k를 만들 수 있는 가장 많은 횟수를 리턴하는 것
# 두 수는 더하고 나면 array에서 사라짐
# solution1 => Time Limit Exceeded
# solution2 -> Time Limit Exceeded
def solution1(nums, k):
    # 1 array를 정렬
    # 2 two pointer 사용
    # 3 k에 맞는 값을 찾는 시행이 있다면 result += 1
    # 4 해당 두 수를 제거 하고 다시 실행(이중 반복문)
    # + check로 한번 돌았는지 확인하고 돌았다면 그대로 반복문 나가기

    arr = sorted(nums)
    result = 0
    check = True

    while len(arr) > 1 and check:
        p1 = 0
        p2 = len(arr) - 1
        check = False
        while p1 < p2:
            s = arr[p1] + arr[p2]
            if s == k:
                arr.pop(p2)
                arr.pop(p1)
                result += 1
                check = True
                break
            elif s > k:
                p2 -= 1
            else:
                p1 += 1

    return result


def solution2(nums, k):
    # 1 array를 정렬
    # 2 two pointer 사용
    # 3 k에 맞는 값을 찾는 시행이 있다면 result += 1
    # 4 해당 두 수를 제거 하고 다시 실행

    arr = sorted(nums)
    p1 = 0
    p2 = len(arr) - 1
    result = 0

    while p1 < p2:
        s = arr[p1] + arr[p2]
        if s == k:
            arr.pop(p2)
            arr.pop(p1)
            p1 = 0
            p2 = len(arr) - 1
            result += 1
        elif s > k:
            p2 -= 1
        else:
            p1 += 1

    return result


def solution3(nums, k):
    # 1 array를 정렬
    # 2 two pointer 사용
    # 3 k에 맞는 값을 찾는 시행이 있다면 result += 1
    # 4 해당 두 수를 제거 하고 다시 실행

    arr = sorted(nums)
    p1 = 0
    p2 = len(arr) - 1
    result = 0

    while p1 < p2:
        s = arr[p1] + arr[p2]
        if s == k:
            p1 += 1
            p2 -= 1
            result += 1
        elif s > k:
            p2 -= 1
        else:
            p1 += 1

    return result


print("case1 :", solution3([3, 1, 3, 4, 3], 6))
print("case2 :", solution3([1, 2, 3, 4], 5))
