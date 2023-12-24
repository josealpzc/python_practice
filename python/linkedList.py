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
    #this methods may change, current implementation goes trough all the linked list to find out 
    #who is the last Node, this migt cause a problem if the size of the list increases.
    #To fix this, it is necesary to create a 'last' variable that points to the last Node of the list.
    def removeLast(self):
        if(self.head):
            print(f"head: {self.head.value}")
            if(self.head.next == None):
                print ('yes None')
                self.head = None
                print (f'head: {self.head} DONE')
            else:
                current = self.head
                while(current.next):
                    previous = current
                    current = current.next
                previous.next=None

            self.size-=1

        else:
            print("You can not remove from an empty list")

    def insertAt(self,value,pos):
        tmp = self.size+1
        if(pos>=1 and pos<=tmp):
            if(self.head):
                if(pos==1):
                    self.insertFirst(value)

                elif(pos==tmp):
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
                    self.size+=1

            else:
                self.head = Node(value)
                self.size+=1
        else:
            tmp = self.size+1
            print(f"Please select a number between 1 and {tmp}")

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
            print("[]")

def main():
    print('MY LINKED LIST!')
if __name__ == '__main__':
    main()
