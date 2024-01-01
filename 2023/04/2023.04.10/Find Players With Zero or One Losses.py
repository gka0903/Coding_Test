def findWinners(matches):
    win = set([])
    lose = set([])
    ex = set([])
    for i in matches:
        win.add(i[0])
        if i[1] not in lose:
            lose.add(i[1])
        else:
            ex.add(i[1])
    lose = lose - ex
    win = win - lose - ex
    win = sorted(list(win))
    lose = sorted(list(lose))
    return [win, lose]


print(findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
