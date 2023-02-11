def flipAndInvertImage(image):
    arr = []
    for i in image:
        number = list(reversed(i))
        invert_image = []
        for j in number:
            if j == 1:
                invert_image.append(0)
            else:
                invert_image.append(1)
        arr.append(invert_image)

    return arr


print(flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
