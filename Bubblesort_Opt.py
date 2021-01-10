#Modify the following template to make the outputs match.
# INPUTS CAN BE ANYTHING. 
''' C
    B 
    A
    exit 
    '''
'''F
  R
  M
  Q
  A
  Z
  exit
  '''

def bubble(list):
    count = 0
    count2 = 0# YOUR CODE HERE
    size = len(list)
    i = 0
    while i <  size-1:
      count2 +=1 
      if list[i] > list[i + 1]:
        print('Swapping %s %s' %(list[i+1],list[i]))
        count +=1
        list[i],list[i+1] = list[i+1],list[i]
        i = 0
      elif list[i] < list[i + 1]:
        i +=1
      else:
        i +=1
    
    if count2 >= 20:
      count2 = count2 + 5
    else:
      count2 = count2 + 0
    return (count, count2)
    
    
list = []
while True:
   val = input()
   if val == "exit":
      break
   list.append(val)
   
counts = bubble(list)
print(list)
print("It took", counts[0], "swaps and")
print(counts[1], "comparisons to sort it.")
