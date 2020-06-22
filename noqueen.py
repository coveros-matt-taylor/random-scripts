def initialize_board(size):
  return [-1] * size

def capturable(board, row, col):
  # horizontal is covered by virtue of 1d array

  # vertical
  for i in range(row):
    if board[i] == col:
      return True
  
  # \ diagonal
  for i in range(row):
    if col - board[i] == row - i:
      return True
  
  # / diagonal
  for i in reversed(range(row)):
    if board[i] - col == row - i:
      return True
  
  return False

def solve(board, row=0):
  if row == size:
    return True
  
  for i in range(size):
    if capturable(board, row, i):
      continue
    board[row] = i
    if (solve(board, row+1)):
      return board
  
  return False

def print_board(board):
  for i in range(size):
    for j in range(size):
      out = 'Q ' if board[i] == j else '- '
      print(out, end='')
    print()

size = 8
test_board = [3, -1, -1, -1]
print(capturable(test_board, 3, 3))
board = initialize_board(size)
board = solve(board, 0)
print_board(board)
size = 8
