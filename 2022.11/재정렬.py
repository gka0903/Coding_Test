def solutions(x):
    words = ''
    numbers = 0
    list_word = list(x)
    list_word.sort()
    print(list_word)
    for i in list_word:
        if ord(i) >= ord('A'):
            words += i
        else:
            numbers += int(i)
    print(words)
    print(numbers)

    return words + str(numbers)


print(solutions('K1KA5CB7'))
