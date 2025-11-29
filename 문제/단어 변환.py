def able_move(cur, target):
    diff_count = 0
    for i in range(len(cur)):
        if cur[i] != target[i]:
            diff_count += 1
    if diff_count == 1:
        return True

    return False


def dfs(cur, target, count, words, visited, n):
    global answer
    # 종료 조건
    if target == cur:
        answer = min(count, answer) if answer is not None else count

    # 단어들 중에서 이동 가능한 것으로 이동
    # 단어 visited 처리 # 백트래킹(함수를 나오면 false 처리)
    for i in range(n):
        if not visited[i]:
            if able_move(cur, words[i]):
                visited[i] = True
                dfs(words[i], target, count + 1, words, visited, n)
                visited[i] = False

    return


def solution(begin, target, words):
    global answer
    answer = None
    n = len(words)
    visited = [False] * n

    # 1. 시작 단어로 dfs
    dfs(begin, target, 0, words, visited, n)

    return 0 if answer is None else answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
