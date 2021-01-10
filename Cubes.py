#Keep reading lines from input until --STOP-- is encountered. Each line represents a cube of integers. Determine if all of the columns of the cube add up to the same number or not. This should work for any size square. See the input/output tests below for details. Use %3d for formatting the totals, %2d for everything else. You will probably need this:myList = someString.split(",") NOTE: SETS OF INPUTS ARE BELOW
import math

def show():
  size = len(myList)
  rule = int(math.sqrt(size))
  for i in range(size):
    myList[i] = int(myList[i])
  total = sum(myList[0::rule])
  checker = 0
  if size == math.pow(rule,2):
    i = 0
    while i <= size:
      new_list = myList[i::rule]
      mark = len(new_list)
      checker = sum(new_list)
      if (mark == rule):
        print('COLUMN %2d:'%(i),end='')
        for row in range(mark):
          print('%2d+'%new_list[row],end='')
        if (checker != total):
          print('= %3d'%checker)
          print('Not a magic square!\n')
          break
        elif (checker == total):
          print('= %3d'%checker)
          checker = 0
          i +=1
          continue
        else:
          print('= %3d'%checker)
          checker = 0
          i +=1
          continue
      elif mark != rule:
        print('MAGIC SQUARE!\n')
        break
  else:
    print('Not a square!\n')
  
  return
someString = input()
while True:
  if someString == '--STOP--':
    break
  elif someString != '--STOP--':
    myList = someString.split(',')
    print('INPUT:',someString)
    show()
    someString = input()
'''
1,2,3,4,4,3,2,1,3,2,1,4,2,3,4,1
1,5,3,4,4,3,2,1,3,2,1,4,2,3,4,1
1,2,3,5,4,3,2,1,3,2,1,4,2,3,4,1
9,8,7,6,5,8,7,6,5,9,7,6,5,9,8,6,5,9,8,7,5,9,8,7,6
9,99,7,6,5,8,7,6,5,9,7,6,5,9,8,6,5,9,8,7,5,9,8,7,6
1,2,3,3,2,1,2,3,1
1,2,3,4,5,6,7,8,9
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
1,2,3,4,4,3,2,1,2,3,4,1,3,2,1,4
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
66,77,88,99,77,88,99,66,88,99,66,77,99,66,77,88
66,77,89,98,78,87,99,66,88,99,66,77,99,66,77,88
66,77,89,98,78,87,99,66,88,99,66,77,99,66,77,88,44
--STOP--
  '''