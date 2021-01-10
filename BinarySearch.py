def binarySearch(x, intList):
    if len(intList) == 1:
        if x == intList[0]:
          return True
        else:
          return False
        

    else:
        n1 = len(intList) // 2
        if x in intList[:n1]:
         return  binarySearch(x,intList[:n1])
        else:
         return  binarySearch(x, intList[n1:] )
        

intList = [ 3, 10, 11, 15, 23, 25, 38, 45, 49, 69, 81]
xList=[45, 13, 4, 60, 23]
out=[]
for x in xList:
    out.append([x, binarySearch(x, intList)])
print(out)
# This should show
# [[45, True], [13, False], [4, False], [60, False], [23, True]]







    

