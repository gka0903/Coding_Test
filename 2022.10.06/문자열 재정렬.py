string = list(input())
string.sort()
print(string)

num_string = 0
str_string = ''
for i in string:
    if ord(i) < ord('A'):
        num_string += int(i)
    else:
        str_string += i

print(str_string + str(num_string))



#K1KA5CB7
