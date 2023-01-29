def plusOne(digits):
    num = ''
    for i in digits:
        num += str(i)
    num = int(num) + 1

    return [int(i) for i in str(num)]


print(plusOne([9]))
