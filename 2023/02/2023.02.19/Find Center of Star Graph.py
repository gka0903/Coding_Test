def findCenter(edges):
    check = edges[0]
    for i in edges[1]:
        if i in check:
            return i


print(findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))
