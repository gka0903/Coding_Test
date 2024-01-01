def reorderList(head):
    answer = []
    for i in range(len(head)):
        if i % 2 == 0:
            word = head.pop(0)
        else:
            word = head.pop()
        answer.append(word)
    return answer




print(reorderList([1, 2, 3, 4, 5]))
