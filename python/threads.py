import threading

def hello():
    print("Hello World!")


#t1 = threading.Thread(target=hello)
#t1.start()

def function1():
    for i in range(1000):
        print('ONE')

def function2():
    for i in range(1000):
        print('TWO')
'''
#call the class Thread within the imported module 'threading'
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

#This threads run in parallel
#Alternates between ONE and TWO
#t1.start()
#t2.start()

#This thread run serially
#You will first see ONE and then TWO.
t1.run()
t2.run()
'''
#WAITING FOR THREADS
def function():
    for i in range(500000):
        print('hello world')

t1 = threading.Thread(target=function)
t1.start()

#Here we wait for the thread to finish 
t1.join()

print("THIS IS THE END!")
