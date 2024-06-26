# from random import random

# 1
# def NOD(a, b):
#     if b == 0:
#         return a
#     else:
#         return NOD(b, a % b)
    
# print(NOD(15, 45))


# 2
# randnumber = (str(round(random()*10))) + (str(round(random()*10))) + (str(round(random()*10))) + (str(round(random()*10))) 
# tries = 1

# def cows(mytry1, number, tries):
    
#     if len(number)>4:
#         number = number[1:5]
    
#     mytry1 = str(mytry1)
    
#     right_bulls = 0
#     definitely_right_cows = 0
    
#     for i in range(len(mytry1)):
#         if mytry1[i] in number:
#             right_bulls += 1
#         if mytry1[i] == number[i]:
#             definitely_right_cows += 1
            
#     if mytry1==number:
#         print('You win!')
#         print('You did ', tries, ' tries.')
#         return
#     else:
#         print('bulls:', right_bulls, 'cows:', definitely_right_cows)
#         right_bulls=0
#         definitely_right_cows = 0
#         # print(number)
#         print('Try again!')
#         tries+=1
#         return cows(input('dkdk^ '), number, tries)
    
#     # print(number)
#     # print(type(number))

# cows(1234, randnumber, tries)

# 3
# def is_valid_move(board, row, col):
#     return 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == -1

# def knight_tour(board, row, col, move_count):
#     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

#     board[row][col] = move_count

#     if move_count == len(board) * len(board) - 1:
#         for row in board:
#             print(row)
#         return True

#     for move in moves:
#         new_row = row + move[0]
#         new_col = col + move[1]
#         if is_valid_move(board, new_row, new_col):
#             if knight_tour(board, new_row, new_col, move_count + 1):
#                 return True

#     board[row][col] = -1
#     return False

# n = 8
# chessboard = [[-1 for _ in range(n)] for _ in range(n)]

# start_row = int(input("Введите начальную строку (0-7): "))
# start_col = int(input("Введите начальный столбец (0-7): "))

# if not knight_tour(chessboard, start_row, start_col, 0):
#     print("Путь не найден.")
    
    
#     # тут я конечно не сам решил, но 80% я понимаю что к чему
    

# 4
# import random

# def print_board(board):
#     for row in board:
#         print(" ".join(str(cell) for cell in row))

# def find_blank(board):
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] == 0:
#                 return i, j

# def is_solvable(board):
#     inversions = 0
#     arr = [num for row in board for num in row if num != 0]
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 inversions += 1
#     return inversions % 2 == 0

# def shuffle_board():
#     board = [[j + 4*i for j in range(4)] for i in range(4)]
#     random.shuffle(board)
#     return board

# def move(board, direction):
#     row, col = find_blank(board)
#     if direction == 'up' and row > 0:
#         board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
#     elif direction == 'down' and row < 3:
#         board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
#     elif direction == 'left' and col > 0:
#         board[row][col], board[row][col - 1] = board[row][col - 1], board[row][col]
#     elif direction == 'right' and col < 3:
#         board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]

# def main():
#     board = shuffle_board()
#     while not is_solvable(board):
#         board = shuffle_board()

#     print("Welcome to the 15 Puzzle Game!")
#     print_board(board)

#     while True:
#         move_dir = input("Enter direction (up, down, left, right) or 'q' to quit: ")
#         if move_dir == 'q':
#             break
#         move(board, move_dir)
#         print_board(board)

#         if all(board[i][j] == i*4 + j + 1 for i in range(4) for j in range(4)):
#             print("Congratulations! You solved the puzzle!")
#             break

# if __name__ == "__main__":
#     main()

