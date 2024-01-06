"""
Author: Jose Lopez
Date: 12/31/2023
Notes: This file contains some examples for practicing recursion.

"""
#Print a decreasing count from 10 to 0 
def decreasing_count(number):
    
    #This is the base condition: once the base condition is raised, the recursive method calls are completed, and
    #the loop ends.
    if(number < 0):
        #Once 'number' is 0, the recursive calls to method end.
        return 0 
    
    #If 'number' is greather than 0, we continue calling the method in a recursive way.
    else:
        print(number)
        decreasing_count(number-1)

#This method return the fibonacci number at a given position starting form 0:
def get_fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1 or number ==2):
        return 1
    else:
        return get_fibonacci(number-1) + get_fibonacci(number-2)

#This method prints the 'n' first numbers of the fibonacci sequence.
def print_fibonacci(n):
    for i in range(n):
        print(get_fibonacci(i))

def fibonacci(number):
    a=0
    b=1 
    cnt=0

    while(cnt<number):
        tmp=a+b
        print(a)
        a=b
        b=tmp
        cnt+=1

print_fibonacci(6)

