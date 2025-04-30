location = input()
move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
y = ord(location[0]) - ord('a') + 1
x = int(location[1])
count = 0
for i in move:
    nx = i[0] + x
    ny = i[1] + y
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        count += 1

print(count)
