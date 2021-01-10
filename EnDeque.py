#  Function specs
#
#  enqueue(value): create a new node with the value,
#                       insert at the last pointer (i.e., self.last)
#
#  x = dequeue() : get the value from the top node, and return as x.
#                  At the same time, delete the top node from the queue.
#

class queue:

    # Do not change the subclass
    class node:
        def __init__(self, value, nextNode):
            self.value = value
            self.nextNode = nextNode

    # Do not change __init__
    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # This creates an extra node with "value"
        # and insert at the top
        # See Sec 7 in the lecture notes
        newNode = self.node(value, None)
        if self.size == 0:
            self.top = self.last = newNode
            self.size += 1

        else:
            self.last.nextNode = newNode
            self.last = newNode
            self.size += 1

    def dequeue(self):
        # This returns self.top.value
        # and at the same time deletes the top node.
        if self.size == 0:
            # it must return an error
            return "error: dequeue from an empty queue"
        elif self.size == 1:
            value = self.top.value
            self.top = self.last = None
            self.size -= 1
            return value

        else:
            # ----- code here ----
            value = self.top.value
            self.top = self.top.nextNode
            self.size -= 1
            return value



# Check the class
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
x = q.dequeue()


output = []
while len(q) > 0:
    x = q.dequeue()
    output.append(x)
print(output)
# This should show [2, 3, 4]
