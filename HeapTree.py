
class priorityQueue:
    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        return self.size

    def parent(self,index):
      if (index > self.size) or (index <=1):
        return None
      else:
        return self.heap[index//2-1]
      
        
    def leftChild(self,index):
      if (index<1) or (2*index > self.size):
        return None
      else:
        return self.heap[2*index-1]
      

    def rightChild(self,index):
      if (index < 1) or (2*index +1 > self.size):
        return None
      else:
        return  self.heap[2*index]
      
    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]
      
         
    def insert(self,x):
      self.size +=1
      self.heap.append(x)
      index = self.size
      while (index > 1) and self.parent(index) < self.heap[index-1]:
        parent = index // 2
        self.swap(index, parent)
        index = parent
       
        
#Test code
h = priorityQueue()
h.insert(10)
print(h.heap)
h.insert(5)
print(h.heap)
h.insert(14)
print(h.heap)
h.insert(9)
print(h.heap)
h.insert(2)
print(h.heap)
h.insert(11)
print(h.heap)
h.insert(6)
print(h.heap)
h.insert(12)
print(h.heap)
h.insert(20)
print(h.heap)
### This should print out
#[10]
#[10, 5]
#[14, 5, 10]
#[14, 9, 10, 5]
#[14, 9, 10, 5, 2]
#[14, 9, 11, 5, 2, 10]
#[14, 9, 11, 5, 2, 10, 6]
#
### Draw the heap on a sheet of paper
#       to see the last line satisfies the heap property


