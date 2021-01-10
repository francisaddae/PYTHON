import random
print(
    '  THIS IS THE PRECIOUS AND ACIENCT GAME\n   '
    '  DO NOT CHEAT NOR TAKE IT FOR GRANTED\n    '
    ' IT IS THE PRECIOUS GAME OF ROCK..PAPER..SCISSORS\n   '
    '       Rock beats Scissors\n   '
    '    Scissors beats Paper\n'
    '      Paper beats Rock\n'
    "CAUTION: Don't get angry when you lose\n")

Question = input(
    '   Do you want to play against a PC or a Human? (PC/HUMAN)   ')
rule = ['rock', 'paper', 'scissors']
pick1, pick2 = '', ''


def runs(num_rounds, p1, p2):
  p1 = input('Enter your pick1: ')
  while True:
    if (Question == 'PC'):
      p2 = random.choice(rule)
      print('PC picks %s' % p2)
      break
    elif (p2 != 'PC'):
      p2 = input('Enter your pick2:   ')
      break
  pick1, pick2 = p1, p2

  if pick1 == pick2:
    runs(num_rounds, p1, p2)
  else:
    pick1, pick2 = p1, p2

  return num_rounds, pick1, pick2


def wins(p1, p2):
  if p1 == 'rock' and (p2 == 'siccors'):
    return p1
  elif p1 == 'siccors' and (p2 == 'paper'):
    return p2
  elif p1 == 'paper' and (p2 == 'rock'):
    return p1
  else:
    return p2


def main(p1, p2):
  W1, W2, WINNER = 0, 0, ''
  h_m_rounds = int(input('NUMBER OF PLAYS: '))
  num_rounds = h_m_rounds
  name1, name2 = p1, p2
  while h_m_rounds > 0:
    num_rounds, p1, p2 = runs(num_rounds, p1, p2)
    WINNER = wins(p1, p2)
    if WINNER == p1 and not(h_m_rounds <= 0):
      W1 += 1
      h_m_rounds -= 1

    elif WINNER == p2 and not(h_m_rounds <= 0):
      W2 += 1
      h_m_rounds -= 1
    else:
      num_rounds += 1
      h_m_rounds += 1

  if (W1 > W2) and (Question == 'PC'):
    print('Congratulations!!!!!!!!!!!!!\n%s has shown that he/she is better than PC\n' % name1)
  elif (W1 > W2) and (Question == 'HUMAN'):
    print('Congratulations %s!!!!\nYou just smashed %s out of the gutter :):):)\n' % (
        name1, name2))
  elif (W2 > W1) and (Question == 'HUMAN'):
    print('Congratulations %s!!!!\nYou just smashed %s out of the gutter :):):)\n' % (
        name2, name1))
  elif (W2 > W1) and (Question == 'PC'):
    print('HAHAHAHA!!!!!!\n!!!!!!!!PC IS ALWAYS BETTER THAN HUMAN INTERLIGENCE!!!!!!!\n')


while True:
  if(Question == 'PC'):
    p1 = input('Enter your name:   ')
    p2 = 'PC'
    main(p1, p2)

  elif (Question == 'HUMAN'):
    number_of_people = int(
        input("Count the number of people you're playing with:"))
    if (number_of_people < 2):
      print('You should have played with the PC or try finding a friend and come bacl again\n')
    elif (number_of_people > 2):
      print('   We are sorry!!!!!\nThis game is meant for two people only\n   ')
    else:
      p1 = input('Enter your name player 1:   ')
      p2 = input('Enter your name player 2:   ')
      main(p1, p2)

  else:
    print("   I'm really sorry, this game isn't meant for you\nPlease try again next time   ")
  Restart = input('   Do you wanna start over? (Y/N)   ')
  if Restart == ('Y' or 'y'):
    Question = input(
        '   Do you want to play against a PC or a Human? (PC/HUMAN)   ')
  elif (Restart == ('N' or 'n')):
    break
