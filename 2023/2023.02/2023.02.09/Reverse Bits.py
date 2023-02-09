def reverseBits(n):
    num = str(n)[::-1]
    return type(int(num, 2))


print(reverseBits('00000010100101000001111010011100'))
