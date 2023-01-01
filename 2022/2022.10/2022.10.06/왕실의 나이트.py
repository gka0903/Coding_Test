location = list(input())
nx = ord(location[0]) - 96
ny = location[1]
answer = 0

move_array = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [-1,2], [1,-2], [-1,-2]]

for i in move_array:
    dx = int(nx) + int(i[0])
    dy = int(ny) + int(i[1])
    
    if dx <= 8 and dx >= 1 and dy <= 8 and dy >= 1:
        answer += 1

print(answer)


