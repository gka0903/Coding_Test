def solution(arr):
    answer = []
    for i in arr:
        if i not in answer or answer[-1] != i:
            answer.append(i)
    return answer



