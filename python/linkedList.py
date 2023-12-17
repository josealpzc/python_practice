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

        self.size+=1

    def insertAt(self,value,pos):
        
        if(pos>=1 and pos<=self.size+1):
            if(self.head):
                if(pos==1):
                    self.insertFirst(value)

                elif(pos==self.size+1):
                    self.insertLast(value)

                else:
                    #If this condition is raised, it meand that the node to be added is not in the first or the last one.
                    current = self.head
                    cnt=1
                    while cnt<pos:
                       previous = current
                       current = current.next
                       cnt+=1
                    
                    newNode = Node(value)

                    previous.next = newNode
                    newNode.next = current

            else:
                self.head = Node(value)
            self.size+=1
        else:
            print(f"Please select a number between 1 and {self.size}")

    def insertLast(self,value):
        if (self.head):
            current = self.head
            while current:
                last = current
                current=current.next 
            last.next = Node(value)
        
        else:
            self.head = Node(value)
        
        self.size+=1
    
    #This method removes the first element of a list.
    def removeFirst(self):
        if(self.head):
            if(self.size==1):
                self.head=None
            else:
                self.head=self.head.next
            print(f"Value removed: {self.head.value}")
            self.size-=1
        else:
            print("You can't remove from an empty list")
        
    def printSize(self):
        print(f"size of the list is: {self.size}")
    
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
    #Create a list with 5 different values
    #  5->9->7->10->2
    mylist = LinkedList()
    for i in range(1,6):
        mylist.insertLast(i)

    mylist.printList()
    mylist.printSize()
    
    mylist.insertAt(20,10)
    mylist.removeFirst()
    mylist.printList()
    '''
    mylist.insertAt('HERE',9)
    mylist.printList()
    mylist.printSize()
    '''
 
    
if __name__ == '__main__':
    main()
