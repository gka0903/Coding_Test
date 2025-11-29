def solution(numbers, target):
    answer = 0

    # dfs 현재 만들어진 수랑 더해진 수(len) 매개변수로 넘기기
    def dfs(number, index):
        nonlocal answer

        # 종료 조건 len == len(numbers)
        # 종료 조건에서 sum == target answer += 1
        if index == len(numbers):
            if number == target:
                answer += 1
            return

        # dfs +, - 넣기
        dfs(number + numbers[index], index + 1, )
        dfs(number - numbers[index], index + 1, )

    dfs(0, 0)

    return answer


print(solution([4, 1, 2, 1], 4))
print(solution([1, 1, 1, 1, 1], 3))
