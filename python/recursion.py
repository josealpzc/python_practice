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

#This method prints fibonnaci serie:
def recursive_fibonacci(number):
    """
    #These are the starting numbers of a fibonacci serie. 
    a=0
    b=1
    #This variable will be used to count from 0 to 'number'

    if(number < 1):
        return 0
    else:
        tmp=a+b
        print(a)
        a=b
        b=tmp
        recursive_fibonacci(number-1)
    """
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

recursive_fibonacci(8)
