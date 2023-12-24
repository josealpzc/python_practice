#Author: Jose Lopez 
#Date: 12/223/2023
#Notes: This script contains an interactive menu for the user play with a linked
#list structure, this should change to a Test implementation rather than just a while loop 
#priting a menu.
import linkedList as ll

run = True 
myList = ll.LinkedList()

while(run):

        print('List:')
        myList.printList()
        print(f'Size: {myList.size}')
        response = int(input("""
        Please select an action to perform:
            1. Insert First
            2. Insert Last
            3. Remove First
            4. Remove Last
            5. Add At
            6. Exit
        """))
        if(response == 1):
            value = int(input("Enter a value:"))
            myList.insertFirst(value)

        elif(response == 2):
            value = int(input("Enter a value:"))
            myList.insertLast(value)

        elif(response == 3):
            myList.removeFirst()

        elif(response == 4):
            myList.removeLast()

        elif(response == 5):
            value = int(input("Enter your node value:"))
            position = int(input(f"Enter a position value:"))
            myList.insertAt(value,position)

        elif(response == 6):
            run=False
        else:
            print('choose a valid number')
