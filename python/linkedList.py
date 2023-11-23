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
    def __init__(self,value):
        self.head = value

    def __init__(self):
        self.head = None

    def insert(self,value):
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
    myLinkedList = LinkedList()  # Create a new object
    myLinkedList.printList()     # print all the values in the linked list

    #add items to the list
    myLinkedList.insert(1)
    myLinkedList.insert(4)
    myLinkedList.printList()     # print the list 
    myLinkedList.insert(10)
    myLinkedList.insert(11)
    myLinkedList.printList()


if __name__ == '__main__':
    main()
