# TIC-TAC-TOE

print("TIC-TAC-TOE")

def print_board(board):
  for row in board:
      print(" | ".join(row))
      print("-" * 9)

def check_winner(board):
  # Check rows
  for row in board:
      if row.count(row[0]) == len(row) and row[0] != ' ':
          return True

  # Check columns
  for col in range(len(board)):
      if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
          return True

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
      return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
      return True

  return False

def is_board_full(board):
  for row in board:
      if ' ' in row:
          return False
  return True

def tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  player = 'X'

  while True:
      print_board(board)
      position = int(input(f"Player {player}, choose a position (1-9): ")) - 1

      if position < 0 or position > 8:
          print("Invalid input. Position must be between 1 and 9.")
          continue

      row = position // 3
      col = position % 3

      if board[row][col] != ' ':
          print("That position is already taken. Try again.")
          continue

      board[row][col] = player

      if check_winner(board):
          print_board(board)
          print(f"Player {player} wins the Game!")
          break

      if is_board_full(board):
          print_board(board)
          print("It's a tie!")
          break

      player = 'O' if player == 'X' else 'X'

tic_tac_toe()