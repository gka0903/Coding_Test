number_list = [6, 2, 4, 3, 1, 5, 7, 9, 8, 0]

for i in range(len(number_list)):
    min_index = i
    for j in range(i + 1, len(number_list)):
        if number_list[min_index] > number_list[j]:
            min_index = j
        number_list[min_index], number_list[i] = number_list[i], number_list[min_index]

print(number_list)
