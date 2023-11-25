#Author: Jose Lopez
#Last Update: 11/23/23
#Comments: This is a linked List structure implementation:
#Classes: Node, LinkedList
#methods: 
#   - Insert
#   - Delete
#   - Size
#Note: see the LinkedList.txt file for more information about this data structure.

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertFirst(self,value):
        if(self.head):
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode 
        else:
            self.head = Node(value)
    
    def insertLast(self,value):
        if (self.head):
            current = self.head
            while current:
                last = current
                current=current.next 
            last.next = Node(value)
        
        else:
            self.head = Node(value)


    def printList(self):

        if(self.head):
            nodes = []
            current = self.head
            while(current):
                nodes.append(current.value)
                current = current.next
            print(nodes)
        else:
            print("List is empty")
        
def main():
    mylist1 = LinkedList()
    mylist2 = LinkedList()

    for i in range (10):
        if(i < 5):
            mylist1.insertLast(i)
        else:
            mylist2.insertLast(i)
    
    mylist1.insertFirst(10)

    mylist1.printList()
    mylist2.printList()


if __name__ == '__main__':
    main()
