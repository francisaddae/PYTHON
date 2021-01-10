# NAME OF ASSIGNMENT:  To display a tic-tac-toe borad on a screen and fill the borad with X
# INPUTS: User inputs of X's
# OUTPUTS: Tic-Tac-Toe board with X
# PROCESS (DESCRIPTION OF ALGORITHM): The use of nested for loops and while loops.
# END OF COMMENTS


# PLACE ANY NEEDED IMPORT STATEMENTS HERE:
import string
import random

def displayBoard(board):
  print(board[0],'|',board[1],'|',board[2],'| ')
  print(board[3],'|',board[4],'|',board[5],'| ')
  print(board[6],'|',board[7],'|',board[8],'| ')

  value = 0
  i = 0
  while i < len(board):
        if board[i] == 'X':
          value +=1
          i +=1
        elif board[i] != 'X':
            break
  return value
def filled(board):
  for i in range(len(board)):
    if board[i] == 'X':
      return True
    elif board[i] != 'X':
      return False


# MAIN PART OF THE PROGRAM
def main():
    board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    i = 0
    while i < len(board):
        board[i] = board.index(board[i]) + 1
        i+=1
    displayBoard(board)
    Move = int(input('Enter move for x (1-9): '))
    print(Move)
    check = 0
    while check <= 8:
        if not(Move in range(1,10)):
            print('Please enter a valid position number 1 through 9')
            displayBoard(board)
            filled(board)
            Move = int(input('Enter move for x (1-9): '))
            print(Move)

        elif (Move in range(1,10)):
            if board[Move-1] == Move:
                board[Move-1] = 'X'
                displayBoard(board)
                filled(board)
                check +=1
                if check > 8:
                    break
                else:
                    Move = int(input('Enter move for x (1-9): '))
                    print(Move)
                    filled(board)
            elif board[Move-1] == 'X':
                print('That position is filled! Try again!')
                displayBoard(board)
                filled(board)
                Move = int(input('Enter move for x (1-9): '))
                print(Move)
    print('End of game!')

main()
''' This fuction works but you do have to observe the final portion of it since the instrctor did some specifications to it.
# INCLUDE THE FOLLOWING 2 LINES, BUT NOTHING ELSE BETWEEN HERE
if __name__ == "__main__":
    main()

# AND HERE'''
