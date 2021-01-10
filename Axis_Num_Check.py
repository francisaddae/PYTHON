#Write a program that asks the user for points on a graph. Determine what quadrant the points are in and display an appropriate message. Keep asking until the origin is entered (0,0). Count how many points were in each quadrant and display the count at the end. If the point is on either axis, display a message and do not count it.


quadrant1 = 0
quadrant2 = 0
quadrant3 = 0
quadrant4 = 0
x = int(input('Enter x: '))
print(x)
y = int(input('Enter y: '))
print(y)
while True:
  if (x > 0) and (y > 0):
    quadrant1 +=1
    print('Quadrant I')
  elif (x < 0) and (y > 0):
    quadrant2 +=1
    print('Quadrant II')
  elif ( x < 0) and (y < 0):
    quadrant3 +=1
    print('Quadrant III')
  elif (x > 0) and (y < 0):
    quadrant4 +=1
    print('Quadrant IV')
  elif ( x == 0 and ( (y < 0) or (y > 0))):
    print('Axis points are skipped.')
  elif ( y == 0 and ( (x < 0) or ( x > 0))):
    print('Axis points are skipped.')
  else:
    print('Axis points are skipped.')
    break
  x = int(input('Enter x: '))
  print(x)
  y = int(input('Enter y: '))
  print(y) 
    
    
print('There were:')
print('%d point(s) in quadrant I, \n%d point(s) in quadrant II,\n%d point(s) in quadrant III,\n%d and point(s) in quadrant IV' %(quadrant1,quadrant2,quadrant3,quadrant4))


      
      
      
      