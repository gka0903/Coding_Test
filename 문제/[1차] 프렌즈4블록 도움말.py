# def solution(m, n, board):
#     answer = 0
#
#     # i + 1 , j + 1, i + 1 j + 1 검사 하는 반복문
#     # while 문으로 반복 해서 조건 만족할 때까지 조건이란 더이상 나누어지지 않을때까지
#
#     check = True
#
#     while check:
#         check = False
#         board_del = set()
#
#         for i in range(m):
#             for j in range(n):
#                 a = (i, j)
#                 b = (i, j + 1) if j + 1 < n else (0, 0)
#
#                 if (b != (0, 0) and c != (0, 0) and d != (0, 0)
#                         and a == board[b[0]][b[1]] and a == board[c[0]][c[1]] and a == board[d[0]][d[1]]):
#                     board_del.add([a, b, c, d])
#
#         if board_del != {}:
#             check = True
#             answer += len(board_del)
#
#             for d in board_del:
#                 for i, j in d:
#                     board[i][j] = -1
#     return answer
