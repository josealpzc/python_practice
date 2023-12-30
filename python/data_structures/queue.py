import linkedList
class Queue(linkedList.LinkedList):
    def __init__(self):
        super().__init__()
        self.front=None
    def enqueue(self,value):
        self.insertFirst(value)

    def dequeue(self):
        self.removeLast()

    def rear(self):
        return self.head.value

    def printQueue(self):
        self.printList()


