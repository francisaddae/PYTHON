#Selection Sort Algorithum
'''i is the starting item of your list'''
''' Find the minimum of the list and swap it with the i respectively'''
my_list = [3,000000.10000,4,1,2,100,1001]
def SelectionSort(my_list):
  size = len(my_list)
  for i in range(size):
    a = i + 1 if i != size -1 else i
    com = min(my_list[a:])
    comp = my_list.index(com)
    if my_list[i] < my_list[comp]:
     continue
    else:
      my_list[i], my_list[comp] = my_list[comp], my_list[i] 
  return my_list

#Insertion Sort Algorithum
'''if x is the starting item, check it with its left neighbours. If x is smaller, Swap them'''
'''Do this till every item is in order'''
def InsertionSort(my_list):
  size = len(my_list)
  for a in range(size):
    b = a 
    while b > 1 and my_list[b-1] > my_list[b]:
      my_list[b-1],my_list[b] = my_list[b],my_list[b-1]
  return my_list


#QuickSort Algorithum
#Modifications now, its a procedural function
def QuickSort(my_list, start, end):
  n = end - start 
  if (n <= 1):
    return my_list
  x, left, right = my_list[start], start, end-1 
  while (left < right):
    if (my_list[left] <= x):
      left += 1 
    else:
      my_list[left],my_list[right] = my_list[right],my_list[left]
      right -= 1 
  if (my_list[left] > x):
    left -= 1 
  my_list[start], my_list[left] = my_list[left],my_list[start]
  QuickSort(my_list, start, left)
  QuickSort(my_list, left+1, end)
  
my_list = [30000,5,4,1,2]
print(SelectionSort(my_list),'*****' , InsertionSort(my_list))
QuickSort(my_list,0, 2)
print(my_list)
print('\n')

#Randomizing mumbers 
import random 
my_list = ans = list(range(1,201))
random.shuffle(my_list)
print(my_list)
print(SelectionSort(my_list)== ans, InsertionSort(my_list)== ans)
QuickSort(my_list,0,200)
print(my_list)
print('\n')

#Pseudo number generator 
random.seed(10,2)
t = random.getstate()
my_list = list(t[1])
print(my_list)
print('\n')

