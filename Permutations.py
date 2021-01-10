# WRITE YOUR CODE UP HERE -- CREATE A
# RECURSIVE FUNCTION THAT PRINTS ALL
# OF THE PERMUTATIONS OF THE LIST THAT 
# IS PASSED IN.
import string 
def perm(start, old_list, size):
  if size == 0:
    return old_list
  else:
    for x in range(size):
      start = old_list[x]
      remainder = old_list[x:] + old_list[x+1:]
      
      
    
              
      
      
    
list = input().split(',')
start = []
perm(start, list, len(list))

