knight = input()
nx = int(ord(knight[0])) - int(ord("a")) + 1
ny = int(knight[1])

knight_move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, -2), (-1, -2), (1, -2)]
move_number = 0

for i in knight_move:
    knight_nx = nx + i[1]
    knight_ny = ny + i[0]
    if knight_nx >= 1 & knight_ny >= 1 & knight_nx <= 8 & knight_ny <= 8:
        move_number += 1

print(move_number)