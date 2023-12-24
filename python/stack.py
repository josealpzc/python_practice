import linkedList
class Stack(linkedList.LinkedList):
    def __init__(self):
        super().__init__()
        
    def push(self,value):
        self.insertFirst(value)
    
    #Returns True if stack is empty
    def IsEmpty():
        if self.size == 0:
            return True

        else:
            return False
    def pop(self):
        self.removeFirst()

    def printStack(self):
        self.printList()
    
    #returns the top element of the stack
    def peek():
        return self.head.value





