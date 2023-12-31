#Author: Jose Lopez
#Last Update: 11/23/23
#Comments: This file contains an implementation for a linked list structure.
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    #Inserts a new node in the first position.
    def insertFirst(self,value):
        if(self.head):
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode 
        else:
            self.head=self.tail = Node(value)

        self.size+=1
    
    def removeLast(self):
        if(self.head):
            if(self.head.next == None):
                self.head = None
                self.tail = None
            else:
                current = self.head
                while(current.next):
                    previous = current
                    current = current.next
                self.tail = previous
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
                if(self.head == 1):
                    self.insertFirst(value)
                else:
                    print('List is empty, you can only insert in the first position')
        else:
            print(f"Please select a number between 1 and {tmp}")

    def insertLast(self,value):
        if (self.head):
            current = self.head
            while current:
                last = current
                current=current.next 
            last.next = Node(value)
            self.tail = last.next
        
        else:
            self.head=self.tail = Node(value)
        
        self.size+=1
    
    #This method removes the first element of a list.
    def removeFirst(self):
        if(self.head):
            if(self.size==1):
                self.head=None
                self.tail=None 
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

