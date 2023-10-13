#This method must print decreasing serie from a 'n' number given by the user to 0. 
def recursive_count(n):        #Number is received by the function 
    if(n < 0):                 #If n is less than 0 we should return 0
        return 0               #return 0
    else:                      #If n is still greather than 0 
        print(n)               #print n
        recursive_count(n-1)   #Use recursion to decrease n value

recursive_count(5) #Function receives a number given by the user


