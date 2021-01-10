import math
def show(width,Board):
  size = len(Board)
  def draw(Board):
    for i in range(size):
      Board[i] = '_|'
      print(Board[i],end='')
      if (i+1) % width == 0:
        print(end='\n')
  draw(Board)
  syn = input('Enter the character to fill with: ')
  print(syn)
  user_want = input('Enter (c)olumns or (r)ows: ')
  print(user_want)
  if user_want == 'r':
    print('Enter a row 1 to %d: ' %width,end='')
    play = int(input())
    
    
  elif user_want == 'c':
    print('Enter a column 1 to %d: '%width,end='')
    play = int(input())
    print(play)
    draw(Board)
    print(end='\n')
  


width = int(input('Enter the width of the square: '))
print(width)
while True:
  Board = []
  for i in range(int(math.pow(width,2))):
    Board.append(i)
  show(width,Board)
  Question = input('Continue (Y/N)? ')
  print(Question)
  if Question == 'Y':
    width = int(input('Enter the width of the square: '))
    print(width)
    
  elif Question == 'N':
    print(end='\n')
    break 
  



